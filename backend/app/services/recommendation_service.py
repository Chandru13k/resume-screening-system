from app.ai.hybrid_matcher import HybridMatcher
from app.repositories.job_search_repository import (
    JobSearchRepository,
)


class RecommendationService:

    def __init__(self, db):

        self.db = db

        self.jobs = JobSearchRepository(db)

    def recommend_jobs(
        self,
        candidate_id: int,
    ):

        recommendations = []

        matcher = HybridMatcher(self.db)

        for job in self.jobs.get_active_jobs():

            ranking = matcher.rank_candidates(job)

            for candidate in ranking:

                if candidate["candidate_id"] != candidate_id:
                    continue

                recommendations.append(

                    {

                        "job_id": job.id,

                        "title": job.title,

                        "company_name": job.company_name,

                        "location": job.location,

                        "overall_score": candidate[
                            "overall_score"
                        ],

                    }

                )

        recommendations.sort(

            key=lambda x: x["overall_score"],

            reverse=True,

        )

        return {

            "recommendations": recommendations

        }