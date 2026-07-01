import re


class SectionDetector:
    """
    Split resume into logical sections.
    """

    SECTION_HEADERS = {
        "summary": [
            "summary",
            "professional summary",
            "profile",
            "objective",
        ],
        "skills": [
            "skills",
            "technical skills",
            "core competencies",
            "technologies",
        ],
        "education": [
            "education",
            "academic",
            "qualification",
            "qualifications",
        ],
        "experience": [
            "experience",
            "work experience",
            "employment",
            "professional experience",
            "internship",
        ],
        "projects": [
            "projects",
            "academic projects",
            "personal projects",
        ],
        "certifications": [
            "certifications",
            "certificates",
            "licenses",
        ],
        "achievements": [
            "achievements",
            "awards",
            "honors",
        ],
        "languages": [
            "languages",
            "language",
        ],
    }

    @classmethod
    def split_sections(cls, text: str) -> dict:

        sections = {}
        current_section = "header"
        buffer = []

        lines = text.splitlines()

        for line in lines:

            clean = line.strip()

            if not clean:
                continue

            detected = cls._detect_heading(clean)

            if detected:

                sections[current_section] = "\n".join(buffer).strip()

                current_section = detected

                buffer = []

                continue

            buffer.append(clean)

        sections[current_section] = "\n".join(buffer).strip()

        return sections

    @classmethod
    def _detect_heading(cls, line: str):

        line = re.sub(r"[^a-zA-Z ]", "", line).lower().strip()

        for section, headings in cls.SECTION_HEADERS.items():

            if line in headings:

                return section

        return None