from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.job import Job


class JobRepository:

    def __init__(self, db: Session):
        self.db = db

    # --------------------------------------------------
    # Create
    # --------------------------------------------------

    def create(
        self,
        job: Job,
    ) -> Job:

        self.db.add(job)

        self.db.flush()

        self.db.refresh(job)

        return job

    # --------------------------------------------------
    # Get By ID
    # --------------------------------------------------

    def get_by_id(
        self,
        job_id: int,
    ) -> Job | None:

        statement = (
            select(Job)
            .where(Job.id == job_id)
        )

        return self.db.scalar(statement)

    # --------------------------------------------------
    # Recruiter Jobs
    # --------------------------------------------------

    def get_by_recruiter(
        self,
        recruiter_id: int,
    ) -> list[Job]:

        statement = (
            select(Job)
            .where(
                Job.recruiter_id == recruiter_id
            )
            .order_by(
                Job.created_at.desc()
            )
        )

        return list(
            self.db.scalars(statement)
        )

    # --------------------------------------------------
    # Public Jobs
    # --------------------------------------------------

    def get_active_jobs(self) -> list[Job]:

        statement = (
            select(Job)
            .where(
                Job.is_active.is_(True),
                Job.status == "OPEN",
            )
            .order_by(
                Job.created_at.desc()
            )
        )

        return list(
            self.db.scalars(statement)
        )

    # --------------------------------------------------
    # Delete
    # --------------------------------------------------

    def delete(
        self,
        job: Job,
    ):

        self.db.delete(job)