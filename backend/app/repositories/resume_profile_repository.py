from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.resume_profile import ResumeProfile


class ResumeProfileRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        profile: ResumeProfile,
    ) -> ResumeProfile:

        self.db.add(profile)
        self.db.flush()
        self.db.refresh(profile)

        return profile

    def get_by_resume_document(
        self,
        resume_document_id: int,
    ) -> ResumeProfile | None:

        statement = select(ResumeProfile).where(
            ResumeProfile.resume_document_id == resume_document_id
        )

        return self.db.scalar(statement)