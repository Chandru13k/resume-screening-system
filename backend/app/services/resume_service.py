from pathlib import Path

from fastapi import HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.models.resume_document import ResumeDocument
from app.models.user import User

from app.repositories.resume_repository import ResumeRepository
from app.repositories.resume_skill_repository import ResumeSkillRepository

from app.schemas.resume import ResumeUploadResponse

from app.utils.file_storage import save_upload_file
from app.utils.text_extractor import TextExtractor

from app.resume_parser.extractor import ResumeExtractor

from app.ai.indexing_service import IndexingService
from app.ai.skill_normalizer import normalize


class ResumeService:

    def __init__(self, db: Session):

        self.db = db

        self.resume_repo = ResumeRepository(db)

        self.resume_skill_repo = ResumeSkillRepository(db)

        self.indexing_service = IndexingService()

    # --------------------------------------------------
    # Upload Resume
    # --------------------------------------------------

    async def upload_resume(
        self,
        file: UploadFile,
        current_user: User,
    ) -> ResumeUploadResponse:

        if current_user.role != "candidate":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only candidates can upload resumes.",
            )

        try:

            (
                stored_filename,
                file_path,
                file_size,
            ) = await save_upload_file(file)

            extracted = TextExtractor.extract(file_path)

            extracted_text = extracted["text"]

            links = extracted["links"]

            resume = ResumeDocument(

                candidate_id=current_user.id,

                original_filename=file.filename,

                stored_filename=stored_filename,

                file_path=file_path,

                file_type=Path(file.filename).suffix.lower(),

                file_size=file_size,

                upload_status="uploaded",

                extracted_text=(
                    extracted_text
                    + "\n\n"
                    + "\n".join(links)
                ),

                parsing_completed=False,

            )

            self.resume_repo.create(resume)

            skills = normalize(

                ResumeExtractor.extract_skills(
                    resume.extracted_text
                )

            )

            self.resume_skill_repo.create_many(
                resume.id,
                skills,
            )

            resume.parsing_completed = True

            self.db.commit()

            self.indexing_service.index_resume(
                resume_id=resume.id,
                candidate_id=resume.candidate_id,
                text=resume.extracted_text,
            )

            self.db.refresh(resume)

            return ResumeUploadResponse.model_validate(
                resume
            )

        except HTTPException:
            self.db.rollback()
            raise

        except Exception as e:
            self.db.rollback()

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )

    # --------------------------------------------------
    # Get Candidate Resumes
    # --------------------------------------------------

    def get_candidate_resumes(
        self,
        candidate_id: int,
    ):
        return self.resume_repo.get_by_candidate(
            candidate_id
        )

    # --------------------------------------------------
    # Get Resume
    # --------------------------------------------------

    def get_resume(
        self,
        resume_id: int,
        candidate_id: int,
    ):

        resume = self.resume_repo.get_by_id(
            resume_id
        )

        if not resume:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resume not found.",
            )

        if resume.candidate_id != candidate_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied.",
            )

        return resume

    # --------------------------------------------------
    # Delete Resume
    # --------------------------------------------------

    def delete_resume(
        self,
        resume_id: int,
        candidate_id: int,
    ):

        resume = self.get_resume(
            resume_id,
            candidate_id,
        )

        path = Path(resume.file_path)

        if path.exists():
            path.unlink()

        self.resume_repo.delete(
            resume
        )

        self.db.commit()