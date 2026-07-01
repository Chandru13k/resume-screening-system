from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.resume_skill import ResumeSkill


class ResumeSkillRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_many(
        self,
        resume_id: int,
        skills: list[str],
    ):

        for skill in skills:

            self.db.add(

                ResumeSkill(
                    resume_id=resume_id,
                    skill=skill,
                )

            )

    def get_by_resume(
        self,
        resume_id: int,
    ) -> list[ResumeSkill]:

        statement = (
            select(ResumeSkill)
            .where(
                ResumeSkill.resume_id == resume_id
            )
            .order_by(
                ResumeSkill.skill
            )
        )

        return list(
            self.db.scalars(statement)
        )