from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.job_skill import JobSkill


class JobSkillRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        job_skill: JobSkill,
    ) -> JobSkill:

        self.db.add(job_skill)
        self.db.flush()
        self.db.refresh(job_skill)

        return job_skill

    def create_many(
        self,
        job_id: int,
        skills: list[str],
    ) -> None:

        for skill in skills:

            self.db.add(

                JobSkill(
                    job_id=job_id,
                    skill=skill,
                )

            )

    def get_by_job(
        self,
        job_id: int,
    ) -> list[JobSkill]:

        statement = (
            select(JobSkill)
            .where(
                JobSkill.job_id == job_id
            )
            .order_by(
                JobSkill.skill
            )
        )

        return list(
            self.db.scalars(statement)
        )

    def get_skills(
        self,
        job_id: int,
    ) -> list[str]:
        """
        Return only the skill names for a job.
        """

        statement = (
            select(JobSkill.skill)
            .where(
                JobSkill.job_id == job_id
            )
            .order_by(
                JobSkill.skill
            )
        )

        return list(
            self.db.scalars(statement)
        )