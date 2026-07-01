import re

from app.parsers.skill_extractor import SkillExtractor


class SkillMatcher:
    """
    Compare job description skills with candidate skills.
    """

    @staticmethod
    def compare(
        job_description: str,
        candidate_skills: list[str],
    ) -> dict:

        # ------------------------------------------
        # Extract skills from Job Description
        # ------------------------------------------

        jd_skills = SkillExtractor.extract(
            job_description
        )

        jd_set = {
            skill.lower()
            for skill in jd_skills
        }

        candidate_set = {
            skill.lower()
            for skill in candidate_skills
        }

        matched = sorted(
            jd_set.intersection(candidate_set)
        )

        missing = sorted(
            jd_set.difference(candidate_set)
        )

        if len(jd_set) == 0:
            score = 0.0
        else:
            score = round(
                (len(matched) / len(jd_set)) * 100,
                2,
            )

        return {

            "job_skills": sorted(jd_set),

            "matched_skills": matched,

            "missing_skills": missing,

            "skill_score": score,
        }