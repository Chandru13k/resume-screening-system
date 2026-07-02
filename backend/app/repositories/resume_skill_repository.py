from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.resume_skill import ResumeSkill


class ResumeSkillRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, resume_skill: ResumeSkill) -> ResumeSkill:
        self.db.add(resume_skill)
        self.db.flush()
        self.db.refresh(resume_skill)
        return resume_skill

    def create_many(
        self,
        resume_id: int,
        skills: list[str],
    ) -> None:

        # Remove duplicates while preserving order
        unique_skills = list(dict.fromkeys(skills))

        for skill in unique_skills:
            self.db.add(
                ResumeSkill(
                    resume_id=resume_id,
                    skill=skill,
                )
            )

    def get_skills(
        self,
        resume_id: int,
    ) -> list[str]:

        statement = (
            select(ResumeSkill.skill)
            .where(
                ResumeSkill.resume_id == resume_id
            )
            .order_by(
                ResumeSkill.skill
            )
        )

        return list(self.db.scalars(statement))