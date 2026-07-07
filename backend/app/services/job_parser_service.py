import re

from app.utils.skill_dictionary import COMMON_SKILLS


class JobParserService:

    @staticmethod
    def extract_skills(
        description: str,
    ) -> list[str]:

        text = description.lower()

        found = set()

        for skill in COMMON_SKILLS:

            pattern = r"\b" + re.escape(skill) + r"\b"

            if re.search(pattern, text):
                found.add(skill.title())

        return sorted(found)