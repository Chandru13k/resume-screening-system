from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.job import Job
from app.models.resume_document import ResumeDocument


class DashboardRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def total_jobs(
        self,
        recruiter_id: int,
    ) -> int:

        statement = (
            select(func.count())
            .select_from(Job)
            .where(
                Job.recruiter_id == recruiter_id
            )
        )

        return self.db.scalar(statement) or 0

    def active_jobs(
        self,
        recruiter_id: int,
    ) -> int:

        statement = (
            select(func.count())
            .select_from(Job)
            .where(
                Job.recruiter_id == recruiter_id,
                Job.is_active.is_(True),
            )
        )

        return self.db.scalar(statement) or 0

    def total_resumes(self) -> int:

        statement = (
            select(func.count())
            .select_from(
                ResumeDocument
            )
            .where(
                ResumeDocument.parsing_completed.is_(True)
            )
        )

        return self.db.scalar(statement) or 0

    def recent_jobs(
        self,
        recruiter_id: int,
        limit: int = 5,
    ):

        statement = (
            select(Job)
            .where(
                Job.recruiter_id == recruiter_id
            )
            .order_by(
                Job.created_at.desc()
            )
            .limit(limit)
        )

        return list(
            self.db.scalars(statement)
        )