from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.job import Job


class JobSearchRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_active_jobs(self) -> list[Job]:

        statement = (
            select(Job)
            .where(Job.is_active.is_(True))
            .order_by(Job.created_at.desc())
        )

        return list(
            self.db.scalars(statement)
        )