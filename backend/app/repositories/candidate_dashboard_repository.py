from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.candidate_profile import CandidateProfile
from app.models.resume_document import ResumeDocument


class CandidateDashboardRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_profile(
        self,
        user_id: int,
    ):

        return self.db.scalar(
            select(CandidateProfile).where(
                CandidateProfile.user_id == user_id
            )
        )

    def get_resumes(
        self,
        user_id: int,
    ):

        statement = (
            select(ResumeDocument)
            .where(
                ResumeDocument.candidate_id == user_id
            )
            .order_by(
                ResumeDocument.created_at.desc()
            )
        )

        return list(
            self.db.scalars(statement)
        )