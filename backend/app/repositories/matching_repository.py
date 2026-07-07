from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.resume_document import ResumeDocument
from app.models.resume_skill import ResumeSkill


class MatchingRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all_completed_resumes(self) -> list[ResumeDocument]:

        statement = (
            select(ResumeDocument)
            .where(
                ResumeDocument.parsing_completed.is_(True)
            )
        )

        return list(
            self.db.scalars(statement)
        )

    def get_resume_skills(
        self,
        resume_id: int,
    ) -> list[str]:

        statement = (
            select(ResumeSkill.skill)
            .where(
                ResumeSkill.resume_id == resume_id
            )
        )

        return list(
            self.db.scalars(statement)
        )