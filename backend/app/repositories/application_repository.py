from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models.application import Application


class ApplicationRepository:

    def __init__(self, db: Session):
        self.db = db

    # --------------------------------------------------
    # Create
    # --------------------------------------------------

    def create(
        self,
        application: Application,
    ) -> Application:
        self.db.add(application)
        self.db.flush()
        self.db.refresh(application)
        return application

    # --------------------------------------------------
    # Get By ID
    # --------------------------------------------------

    def get_by_id(
        self,
        application_id: int,
    ) -> Application | None:
        statement = (
            select(Application)
            .where(Application.id == application_id)
            .options(
                joinedload(Application.job),
                joinedload(Application.resume),
                joinedload(Application.candidate),
            )
        )
        return self.db.scalar(statement)

    # --------------------------------------------------
    # Already Applied?
    # --------------------------------------------------

    def get_by_job_and_candidate(
        self,
        job_id: int,
        candidate_id: int,
    ) -> Application | None:
        statement = (
            select(Application)
            .where(
                Application.job_id == job_id,
                Application.candidate_id == candidate_id,
            )
        )
        return self.db.scalar(statement)

    # --------------------------------------------------
    # Candidate Applications
    # --------------------------------------------------

    def get_by_candidate(
        self,
        candidate_id: int,
    ) -> list[Application]:
        statement = (
            select(Application)
            .where(Application.candidate_id == candidate_id)
            .options(
                joinedload(Application.job),
                joinedload(Application.resume),
            )
            .order_by(Application.applied_at.desc())
        )
        return list(self.db.scalars(statement))

    # --------------------------------------------------
    # Recruiter Applications
    # --------------------------------------------------

    def get_by_job(
        self,
        job_id: int,
    ) -> list[Application]:
        statement = (
            select(Application)
            .where(Application.job_id == job_id)
            .options(
                joinedload(Application.job),
                joinedload(Application.resume),
                joinedload(Application.candidate),
            )
            .order_by(Application.applied_at.desc())
        )
        return list(self.db.scalars(statement))

    # --------------------------------------------------
    # Update Status
    # --------------------------------------------------

    def update_status(
        self,
        application: Application,
        status,
    ) -> Application:
        application.status = status
        self.db.flush()
        self.db.refresh(application)
        return application
