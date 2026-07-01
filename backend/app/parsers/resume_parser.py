from app.parsers.entity_extractor import EntityExtractor
from app.parsers.section_detector import SectionDetector
from app.parsers.skill_extractor import SkillExtractor


class ResumeParser:
    """
    Main resume parser.

    Converts raw resume text into structured data.
    """

    @classmethod
    def parse(cls, text: str) -> dict:

        sections = SectionDetector.split_sections(text)

        header = sections.get("header", "")
        summary = sections.get("summary", "")

        return {

            # ---------- Basic Details ----------

            "full_name": EntityExtractor.extract_name(header),

            "email": EntityExtractor.extract_email(text),

            "phone": EntityExtractor.extract_phone(text),

            "location": EntityExtractor.extract_location(header),

            "summary": summary,

            # ---------- Links ----------

            "github_url": EntityExtractor.extract_github(text),

            "linkedin_url": EntityExtractor.extract_linkedin(text),

            "portfolio_url": EntityExtractor.extract_portfolio(text),

            "coding_profiles": EntityExtractor.extract_coding_profiles(text),

            # ---------- Sections ----------

            "skills": SkillExtractor.extract(
                sections.get("skills", text)
            ),

            "education": cls.parse_education(
                sections.get("education", "")
            ),

            "experience": cls.parse_experience(
                sections.get("experience", "")
            ),

            "projects": cls.parse_projects(
                sections.get("projects", "")
            ),

            "certifications": cls.parse_certifications(
                sections.get("certifications", "")
            ),

            "languages": cls.parse_list(
                sections.get("languages", "")
            ),

            "achievements": cls.parse_list(
                sections.get("achievements", "")
            ),
        }

    # -------------------------------------------------
    # Generic List Parser
    # -------------------------------------------------

    @staticmethod
    def parse_list(section: str):

        if not section:
            return []

        items = []

        for line in section.splitlines():

            line = line.strip("•-* ").strip()

            if not line:
                continue

        # Ignore hyperlinks
            if line.startswith("http"):
                continue

        # Ignore mail links
            if line.startswith("mailto:"):
                continue
             # Split comma-separated values
            if "," in line:

                parts = [
                    part.strip()
                    for part in line.split(",")
                    if part.strip()
                ]

                items.extend(parts)
            else:

                items.append(line)

        return items

    # -------------------------------------------------
    # Education
    # -------------------------------------------------

    @classmethod
    def parse_education(cls, section: str):

        return cls.parse_list(section)

    # -------------------------------------------------
    # Experience
    # -------------------------------------------------

    @classmethod
    def parse_experience(cls, section: str):

        return cls.parse_list(section)

    # -------------------------------------------------
    # Projects
    # -------------------------------------------------

    @classmethod
    def parse_projects(cls, section: str):

        return cls.parse_list(section)

    # -------------------------------------------------
    # Certifications
    # -------------------------------------------------

    @classmethod
    def parse_certifications(cls, section: str):

        return cls.parse_list(section)