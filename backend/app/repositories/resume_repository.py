from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.resume_document import ResumeDocument


class ResumeRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        resume: ResumeDocument,
    ) -> ResumeDocument:

        self.db.add(resume)
        self.db.flush()
        self.db.refresh(resume)

        return resume

    def get_by_id(
        self,
        resume_id: int,
    ) -> ResumeDocument | None:

        statement = (
            select(ResumeDocument)
            .where(ResumeDocument.id == resume_id)
        )

        return self.db.scalar(statement)

    def get_by_candidate(
        self,
        candidate_id: int,
    ) -> list[ResumeDocument]:

        statement = (
            select(ResumeDocument)
            .where(
                ResumeDocument.candidate_id == candidate_id
            )
            .order_by(
                ResumeDocument.created_at.desc()
            )
        )

        return list(self.db.scalars(statement))

    def delete(
        self,
        resume: ResumeDocument,
    ):

        self.db.delete(resume)