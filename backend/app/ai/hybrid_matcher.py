from app.ai.semantic_matcher import SemanticMatcher
from app.repositories.job_skill_repository import JobSkillRepository
from app.repositories.resume_skill_repository import ResumeSkillRepository


class HybridMatcher:
    """
    Combines semantic similarity, skill overlap,
    and resume completeness into a final score.
    """

    def __init__(self, db):

        self.db = db

        self.semantic = SemanticMatcher()

        self.job_skill_repo = JobSkillRepository(db)

        self.resume_skill_repo = ResumeSkillRepository(db)

    def rank_candidates(
        self,
        job,
    ):

        semantic_results = self.semantic.search(
            job.description,
            limit=25,
        )

        job_skills = set(
            self.job_skill_repo.get_skills(job.id)
        )

        ranked = []

        for candidate in semantic_results:

            resume_skills = set(
                self.resume_skill_repo.get_skills(
                    candidate["resume_id"]
                )
            )

            matched = job_skills & resume_skills

            if len(job_skills):

                skill_score = (
                    len(matched)
                    / len(job_skills)
                ) * 100

            else:

                skill_score = 0

            completeness = min(
                len(resume_skills) * 5,
                100,
            )

            final_score = round(

                (
                    candidate["semantic_score"] * 0.60
                    + skill_score * 0.30
                    + completeness * 0.10
                ),

                2,
            )

            ranked.append(

                {
                    "candidate_id": candidate["candidate_id"],
                    "resume_id": candidate["resume_id"],
                    "semantic_score": round(
                        candidate["semantic_score"],
                        2,
                    ),
                    "skill_score": round(
                        skill_score,
                        2,
                    ),
                    "resume_completeness": completeness,
                    "overall_score": final_score,
                    "matched_skills": sorted(
                        list(matched)
                    ),
                    "missing_skills": sorted(
                        list(job_skills - resume_skills)
                    ),
                }

            )

        ranked.sort(

            key=lambda x: x["overall_score"],

            reverse=True,

        )

        return ranked