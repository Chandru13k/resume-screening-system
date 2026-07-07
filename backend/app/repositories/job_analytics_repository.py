from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.job import Job


class JobAnalyticsRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_job(
        self,
        job_id: int,
    ):

        return self.db.scalar(
            select(Job).where(Job.id == job_id)
        )