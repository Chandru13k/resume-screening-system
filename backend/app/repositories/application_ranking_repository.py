from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.application import Application


class ApplicationRankingRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_applications_for_job(
        self,
        job_id: int,
    ) -> list[Application]:

        statement = (
            select(Application)
            .where(
                Application.job_id == job_id
            )
        )

        return list(
            self.db.scalars(statement)
        )