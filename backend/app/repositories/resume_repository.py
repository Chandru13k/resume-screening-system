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

        return self.db.get(
            ResumeDocument,
            resume_id,
        )

    def get_by_candidate(
        self,
        candidate_id: int,
    ) -> list[ResumeDocument]:

        return (
            self.db.query(ResumeDocument)
            .filter(
                ResumeDocument.candidate_id == candidate_id
            )
            .order_by(
                ResumeDocument.created_at.desc()
            )
            .all()
        )