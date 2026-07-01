import re

from app.utils.skill_dictionary import COMMON_SKILLS


class ResumeExtractor:

    @staticmethod
    def extract_skills(
        text: str,
    ) -> list[str]:

        text = text.lower()

        skills = set()

        for skill in COMMON_SKILLS:

            pattern = r"\b" + re.escape(skill) + r"\b"

            if re.search(pattern, text):

                skills.add(skill.title())

        return sorted(skills)