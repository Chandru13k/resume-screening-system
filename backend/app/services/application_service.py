from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.enums.application_status import ApplicationStatus
from app.models.application import Application
from app.repositories.application_repository import ApplicationRepository
from app.repositories.job_repository import JobRepository
from app.repositories.resume_repository import ResumeRepository


class ApplicationService:

    def __init__(self, db: Session):
        self.db = db
        self.application_repo = ApplicationRepository(db)
        self.job_repo = JobRepository(db)
        self.resume_repo = ResumeRepository(db)

    # --------------------------------------------------
    # Apply to Job
    # --------------------------------------------------

    def apply_to_job(
        self,
        job_id: int,
        candidate_id: int,
        resume_id: int,
    ) -> Application:

        job = self.job_repo.get_by_id(job_id)

        if not job:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found.",
            )

        if not job.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Job is no longer accepting applications.",
            )

        resume = self.resume_repo.get_by_id(resume_id)

        if not resume:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resume not found.",
            )

        if resume.candidate_id != candidate_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can only apply using your own resume.",
            )

        existing = self.application_repo.get_by_job_and_candidate(
            job_id=job_id,
            candidate_id=candidate_id,
        )

        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="You have already applied for this job.",
            )

        application = Application(
            job_id=job_id,
            candidate_id=candidate_id,
            resume_id=resume_id,
            status=ApplicationStatus.APPLIED,
        )

        try:
            self.application_repo.create(application)
            self.db.commit()
            self.db.refresh(application)
            return application

        except Exception:
            self.db.rollback()
            raise

    # --------------------------------------------------
    # Candidate Applications
    # --------------------------------------------------

    def get_candidate_applications(
        self,
        candidate_id: int,
    ):
        applications = self.application_repo.get_by_candidate(candidate_id)

        result = []

        for application in applications:
            result.append(
                {
                    "application_id": application.id,
                    "job_id": application.job.id,
                    "job_title": application.job.title,
                    "company_name": application.job.company_name,
                    "location": application.job.location,
                    "status": application.status,
                    "applied_at": application.applied_at,
                }
            )

        return result

    # --------------------------------------------------
    # Recruiter Applications
    # --------------------------------------------------

    def get_job_applications(
        self,
        recruiter_id: int,
        job_id: int,
    ):
        job = self.job_repo.get_by_id(job_id)

        if not job:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found.",
            )

        if job.recruiter_id != recruiter_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied.",
            )

        return self.application_repo.get_by_job(job_id)

    # --------------------------------------------------
    # Update Status
    # --------------------------------------------------

    def update_status(
        self,
        recruiter_id: int,
        application_id: int,
        status_value: ApplicationStatus,
    ):
        application = self.application_repo.get_by_id(application_id)

        if not application:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Application not found.",
            )

        if application.job.recruiter_id != recruiter_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied.",
            )

        try:
            self.application_repo.update_status(application, status_value)
            self.db.commit()
            self.db.refresh(application)

            return {
                "application_id": application.id,
                "status": application.status,
                "message": "Application submitted successfully.",
            }

        except Exception:
            self.db.rollback()
            raise
