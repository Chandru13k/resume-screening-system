import shutil
import uuid
from pathlib import Path

from fastapi import HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.models.resume_document import ResumeDocument
from app.repositories.resume_repository import ResumeRepository
from app.repositories.resume_skill_repository import ResumeSkillRepository

from app.resume_parser.parser import ResumeParser
from app.resume_parser.extractor import ResumeExtractor

from app.ai.indexing_service import IndexingService


UPLOAD_DIR = Path("uploads/resumes")


class ResumeService:

    def __init__(self, db: Session):

        self.db = db

        self.resume_repo = ResumeRepository(db)

        self.resume_skill_repo = ResumeSkillRepository(db)

        self.indexing_service = IndexingService()

        UPLOAD_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

    # --------------------------------------------------
    # Upload Resume
    # --------------------------------------------------

    def upload_resume(
        self,
        candidate_id: int,
        file: UploadFile,
    ) -> ResumeDocument:

        extension = Path(file.filename).suffix.lower()

        if extension not in [".pdf", ".docx"]:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only PDF and DOCX resumes are supported.",
            )

        stored_filename = (
            f"{uuid.uuid4()}{extension}"
        )

        file_path = (
            UPLOAD_DIR / stored_filename
        )

        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer,
            )

        resume = ResumeDocument(

            candidate_id=candidate_id,

            original_filename=file.filename,

            stored_filename=stored_filename,

            file_path=str(file_path),

            parsing_completed=False,

        )

        try:

            self.resume_repo.create(resume)

            # -----------------------------
            # Parse Resume
            # -----------------------------

            extracted_text = ResumeParser.parse(
                str(file_path)
            )

            resume.extracted_text = extracted_text

            skills = ResumeExtractor.extract_skills(
                extracted_text
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

            return resume

        except Exception:

            self.db.rollback()

            raise

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

        path = Path(
            resume.file_path
        )

        if path.exists():

            path.unlink()

        self.resume_repo.delete(
            resume
        )

        self.db.commit()