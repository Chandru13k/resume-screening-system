from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.ai.embedding_service import EmbeddingService
from app.ai.qdrant_service import QdrantService
from app.models.resume_document import ResumeDocument
from app.models.resume_profile import ResumeProfile
from app.parsers.resume_parser import ResumeParser
from app.repositories.resume_profile_repository import ResumeProfileRepository
from app.schemas.resume_profile import ResumeProfileResponse


class ResumeProfileService:

    def __init__(self, db: Session):

        self.db = db

        self.repo = ResumeProfileRepository(db)

        self.embedding_service = EmbeddingService()

        self.qdrant = QdrantService()

    def parse_resume(
        self,
        resume: ResumeDocument,
    ) -> ResumeProfileResponse:

        existing = self.repo.get_by_resume_document(
            resume.id
        )

        if existing:
            return ResumeProfileResponse.model_validate(existing)

        if not resume.extracted_text:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Resume text not available.",
            )

        parsed = ResumeParser.parse(
            resume.extracted_text
        )

        profile = ResumeProfile(

            resume_document_id=resume.id,

            **parsed,
        )

        self.repo.create(profile)

        self.db.commit()

        self.db.refresh(profile)

        # ---------------------------------------
        # Generate Embedding
        # ---------------------------------------

        vector = self.embedding_service.encode(
            resume.extracted_text
        )

        # ---------------------------------------
        # Upload to Qdrant
        # ---------------------------------------

        payload = {

            "resume_document_id": resume.id,

            "candidate_id": resume.candidate_id,

            "full_name": profile.full_name,

            "email": profile.email,

            "skills": profile.skills,

            "location": profile.location,

        }

        self.qdrant.upload_resume_vector(

            resume.id,

            vector,

            payload,
        )

        return ResumeProfileResponse.model_validate(
            profile
        )