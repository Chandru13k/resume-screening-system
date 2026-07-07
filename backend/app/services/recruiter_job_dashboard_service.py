from sqlalchemy.orm import Session

from app.services.application_ranking_service import (
    ApplicationRankingService,
)
from app.repositories.application_repository import (
    ApplicationRepository,
)
from app.repositories.job_repository import JobRepository


class RecruiterJobDashboardService:

    def __init__(self, db: Session):

        self.db = db

        self.job_repo = JobRepository(db)

        self.application_repo = (
            ApplicationRepository(db)
        )

        self.ranking_service = (
            ApplicationRankingService(db)
        )

    def get_dashboard(
        self,
        recruiter_id: int,
        job_id: int,
    ):

        job = self.job_repo.get_by_id(job_id)

        if job.recruiter_id != recruiter_id:
            raise Exception("Access denied")

        applications = self.application_repo.get_by_job(
            job_id
        )

        ranked = self.ranking_service.rank_applicants(
            recruiter_id,
            job_id,
        )

        return {

            "job": {
                "id": job.id,
                "title": job.title,
                "company": job.company_name,
                "status": job.status,
            },

            "statistics": {

                "applications": len(applications),

                "shortlisted": sum(
                    a.status == "SHORTLISTED"
                    for a in applications
                ),

                "interview": sum(
                    a.status == "INTERVIEW"
                    for a in applications
                ),

                "rejected": sum(
                    a.status == "REJECTED"
                    for a in applications
                ),

                "hired": sum(
                    a.status == "HIRED"
                    for a in applications
                ),

            },

            "ranking": ranked["candidates"],

        }