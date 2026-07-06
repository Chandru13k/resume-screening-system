from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.ai.hybrid_matcher import HybridMatcher
from app.repositories.application_ranking_repository import (
    ApplicationRankingRepository,
)
from app.repositories.job_repository import JobRepository
from app.repositories.resume_repository import ResumeRepository


class ApplicationRankingService:

    def __init__(self, db: Session):

        self.db = db

        self.application_repo = (
            ApplicationRankingRepository(db)
        )

        self.job_repo = JobRepository(db)

        self.resume_repo = ResumeRepository(db)

        self.matcher = HybridMatcher(db)

    # --------------------------------------------------
    # Rank Applicants
    # --------------------------------------------------

    def rank_applicants(
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

        applications = (
            self.application_repo.get_applications_for_job(
                job_id
            )
        )

        if len(applications) == 0:
            return {
                "job_id": job_id,
                "candidates": [],
            }

        candidates = []

        for application in applications:

            result = self.matcher.match_candidate(
                job_id=job_id,
                resume_id=application.resume_id,
            )

            result["application_id"] = application.id
            result["candidate_id"] = application.candidate_id
            result["status"] = application.status

            candidates.append(result)

        candidates.sort(
            key=lambda x: x["overall_score"],
            reverse=True,
        )

        return {
            "job_id": job_id,
            "job_title": job.title,
            "total_applicants": len(candidates),
            "candidates": candidates,
        }