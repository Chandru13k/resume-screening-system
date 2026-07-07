from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.job import Job
from app.repositories.job_repository import JobRepository
from app.repositories.job_skill_repository import JobSkillRepository
from app.schemas.job import (
    JobCreateRequest,
    JobUpdateRequest,
)
from app.services.job_parser_service import JobParserService
from app.ai.skill_normalizer import normalize


class JobService:

    def __init__(self, db: Session):
        self.db = db
        self.job_repo = JobRepository(db)
        self.job_skill_repo = JobSkillRepository(db)

    # --------------------------------------------------
    # Create Job
    # --------------------------------------------------
    def create_job(
        self,
        recruiter_id: int,
        data: JobCreateRequest,
    ) -> Job:

        try:
            job = Job(
                recruiter_id=recruiter_id,
                title=data.title,
                company_name=data.company_name,
                location=data.location,
                work_mode=data.work_mode,
                employment_type=data.employment_type,
                experience_required=data.experience_required,
                salary_min=data.salary_min,
                salary_max=data.salary_max,
                total_positions=data.total_positions,
                application_deadline=data.application_deadline,
                description=data.description,
            )

            self.job_repo.create(job)

            # Normalize skills before saving
            skills = normalize(
                JobParserService.extract_skills(
                    data.description
                )
            )

            self.job_skill_repo.create_many(
                job.id,
                skills,
            )

            self.db.commit()
            self.db.refresh(job)

            return job

        except Exception:
            self.db.rollback()
            raise

    # --------------------------------------------------
    # Get All Recruiter Jobs
    # --------------------------------------------------
    def get_jobs(
        self,
        recruiter_id: int,
    ):
        return self.job_repo.get_by_recruiter(recruiter_id)

    # --------------------------------------------------
    # Get One Job
    # --------------------------------------------------
    def get_job(
        self,
        job_id: int,
        recruiter_id: int,
    ) -> Job:

        job = self.job_repo.get_by_id(job_id)

        if not job:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found.",
            )

        if job.recruiter_id != recruiter_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not allowed to access this job.",
            )

        return job

    # --------------------------------------------------
    # Browse Public Jobs
    # --------------------------------------------------
    def get_public_jobs(
        self,
    ):
        return self.job_repo.get_active_jobs()

    # --------------------------------------------------
    # Update Job
    # --------------------------------------------------
    def update_job(
        self,
        job_id: int,
        recruiter_id: int,
        data: JobUpdateRequest,
    ) -> Job:

        job = self.get_job(job_id, recruiter_id)

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(job, key, value)

        self.db.commit()
        self.db.refresh(job)

        return job

    # --------------------------------------------------
    # Delete Job
    # --------------------------------------------------
    def delete_job(
        self,
        job_id: int,
        recruiter_id: int,
    ):
        job = self.get_job(job_id, recruiter_id)
        self.db.delete(job)
        self.db.commit()
