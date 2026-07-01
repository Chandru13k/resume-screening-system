from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.job import Job


class JobRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, job: Job) -> Job:
        self.db.add(job)
        self.db.flush()
        self.db.refresh(job)
        return job

    def get_by_id(self, job_id: int) -> Job | None:
        statement = select(Job).where(Job.id == job_id)
        return self.db.scalar(statement)

    def get_all(self) -> list[Job]:
        statement = select(Job).order_by(Job.created_at.desc())
        return list(self.db.scalars(statement))

    def get_by_recruiter(self, recruiter_id: int) -> list[Job]:
        statement = (
            select(Job)
            .where(Job.recruiter_id == recruiter_id)
            .order_by(Job.created_at.desc())
        )
        return list(self.db.scalars(statement))

    def delete(self, job: Job) -> None:
        self.db.delete(job)