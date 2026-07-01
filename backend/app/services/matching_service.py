from app.repositories.job_repository import JobRepository
from app.repositories.job_skill_repository import JobSkillRepository
from app.repositories.matching_repository import MatchingRepository


class MatchingService:

    def __init__(self, db):

        self.db = db

        self.job_repo = JobRepository(db)

        self.job_skill_repo = JobSkillRepository(db)

        self.matching_repo = MatchingRepository(db)

    # --------------------------------------------------
    # Match Candidates
    # --------------------------------------------------

    def match_candidates(
        self,
        job_id: int,
    ):

        job = self.job_repo.get_by_id(job_id)

        if not job:

            raise ValueError("Job not found.")

        job_skills = set(

            self.job_skill_repo.get_skills(
                job_id
            )

        )

        resumes = (
            self.matching_repo
            .get_all_completed_resumes()
        )

        results = []

        for resume in resumes:

            resume_skills = set(

                self.matching_repo
                .get_resume_skills(
                    resume.id
                )

            )

            matched = sorted(

                list(

                    job_skills &
                    resume_skills

                )

            )

            missing = sorted(

                list(

                    job_skills -
                    resume_skills

                )

            )

            if len(job_skills):

                percentage = round(

                    len(matched)

                    /

                    len(job_skills)

                    *

                    100,

                    2,

                )

            else:

                percentage = 0

            results.append(

                {

                    "candidate_id": resume.candidate_id,

                    "resume_id": resume.id,

                    "matched_skills": matched,

                    "missing_skills": missing,

                    "skill_match_percentage": percentage,

                    "overall_score": percentage,

                }

            )

        results.sort(

            key=lambda x: x["overall_score"],

            reverse=True,

        )

        return {

            "candidates": results

        }