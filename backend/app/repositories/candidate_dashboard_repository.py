from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.application import Application
from app.models.candidate_profile import CandidateProfile
from app.models.job import Job
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

    # --------------------------------------------------
    # Total Applications
    # --------------------------------------------------

    def get_application_count(
        self,
        user_id: int,
    ):

        return (
            self.db.scalar(
                select(func.count())
                .select_from(Application)
                .where(
                    Application.candidate_id == user_id
                )
            )
            or 0
        )

    # --------------------------------------------------
    # Available Jobs
    # --------------------------------------------------

    def get_jobs_available_count(
        self,
    ):

        return (
            self.db.scalar(
                select(func.count())
                .select_from(Job)
                .where(Job.is_active == True)
            )
            or 0
        )