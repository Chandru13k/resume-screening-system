from pathlib import Path

from fastapi import HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.models.resume_document import ResumeDocument
from app.models.user import User
from app.repositories.resume_repository import ResumeRepository
from app.schemas.resume import ResumeUploadResponse
from app.utils.file_storage import save_upload_file
from app.utils.text_extractor import TextExtractor


class ResumeService:

    def __init__(self, db: Session):

        self.db = db
        self.resume_repo = ResumeRepository(db)

    async def upload_resume(
        self,
        file: UploadFile,
        current_user: User,
    ) -> ResumeUploadResponse:
        """
        Upload resume, save it to disk,
        extract text and store metadata.
        """

        # Only candidates can upload resumes
        if current_user.role != "candidate":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only candidates can upload resumes.",
            )

        try:

            # ----------------------------------------
            # Save File
            # ----------------------------------------

            (
                stored_filename,
                file_path,
                file_size,
            ) = await save_upload_file(file)

            # ----------------------------------------
            # Extract Text
            # ----------------------------------------

            extracted = TextExtractor.extract(file_path)

            extracted_text = extracted["text"]

            links = extracted["links"]

            # ----------------------------------------
            # Create Database Record
            # ----------------------------------------

            resume = ResumeDocument(
                candidate_id=current_user.id,
                original_filename=file.filename,
                stored_filename=stored_filename,
                file_path=file_path,
                file_type=Path(file.filename).suffix.lower(),
                file_size=file_size,
                upload_status="uploaded",
                extracted_text=extracted_text + "\n\n" + "\n".join(links),
            )

            self.resume_repo.create(resume)

            self.db.commit()

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