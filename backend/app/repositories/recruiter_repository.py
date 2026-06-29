from sqlalchemy.orm import Session

from app.models.recruiter_profile import RecruiterProfile


class RecruiterRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        profile: RecruiterProfile
    ) -> RecruiterProfile:

        self.db.add(profile)
        self.db.flush()
        self.db.refresh(profile)

        return profile