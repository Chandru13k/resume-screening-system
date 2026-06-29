from sqlalchemy.orm import Session

from app.models.candidate_profile import CandidateProfile


class CandidateRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        profile: CandidateProfile
    ) -> CandidateProfile:

        self.db.add(profile)
        self.db.flush()
        self.db.refresh(profile)

        return profile