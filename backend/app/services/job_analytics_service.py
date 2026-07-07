from app.ai.hybrid_matcher import HybridMatcher
from app.repositories.job_analytics_repository import JobAnalyticsRepository


class JobAnalyticsService:

    def __init__(self, db):

        self.db = db

        self.repo = JobAnalyticsRepository(db)

    def analytics(
        self,
        job_id: int,
    ):

        job = self.repo.get_job(job_id)

        if not job:

            raise ValueError("Job not found.")

        ranking = HybridMatcher(
            self.db
        ).rank_candidates(job)

        if ranking:

            scores = [
                c["overall_score"]
                for c in ranking
            ]

            avg = round(
                sum(scores) / len(scores),
                2,
            )

            top = max(scores)

            recommended = len(
                [
                    c
                    for c in ranking
                    if c["overall_score"] >= 70
                ]
            )

        else:

            avg = 0

            top = 0

            recommended = 0

        return {

            "job_id": job.id,

            "job_title": job.title,

            "total_candidates": len(
                ranking
            ),

            "average_match_score": avg,

            "top_score": top,

            "recommended_for_interview": recommended,

        }