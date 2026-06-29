from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.enums.user_role import UserRole
from app.models.candidate_profile import CandidateProfile
from app.models.recruiter_profile import RecruiterProfile
from app.models.user import User
from app.repositories.candidate_repository import CandidateRepository
from app.repositories.recruiter_repository import RecruiterRepository
from app.repositories.user_repository import UserRepository
from app.schemas.auth import (
    CandidateRegisterRequest,
    RecruiterRegisterRequest,
)
from app.security.password import hash_password


class AuthService:

    def __init__(self, db: Session):
        self.db = db

        self.user_repo = UserRepository(db)
        self.candidate_repo = CandidateRepository(db)
        self.recruiter_repo = RecruiterRepository(db)

    # -----------------------------
    # Candidate Registration
    # -----------------------------
    def register_candidate(
        self,
        data: CandidateRegisterRequest,
    ) -> User:

        existing = self.user_repo.get_by_email(data.email)

        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered."
            )

        try:

            user = User(
                email=data.email,
                password_hash=hash_password(data.password),
                role=UserRole.CANDIDATE,
            )

            self.user_repo.create(user)

            profile = CandidateProfile(
                user_id=user.id,
                full_name=data.full_name,
                phone=data.phone,
                location=data.location,
                github_url=data.github_url,
                linkedin_url=data.linkedin_url,
                portfolio_url=data.portfolio_url,
                coding_profiles=data.coding_profiles,
            )

            self.candidate_repo.create(profile)

            self.db.commit()

            self.db.refresh(user)

            return user

        except Exception:
            self.db.rollback()
            raise

    # -----------------------------
    # Recruiter Registration
    # -----------------------------
    def register_recruiter(
        self,
        data: RecruiterRegisterRequest,
    ) -> User:

        existing = self.user_repo.get_by_email(data.email)

        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered."
            )

        try:

            user = User(
                email=data.email,
                password_hash=hash_password(data.password),
                role=UserRole.RECRUITER,
            )

            self.user_repo.create(user)

            profile = RecruiterProfile(
                user_id=user.id,
                recruiter_name=data.recruiter_name,
                company_name=data.company_name,
                designation=data.designation,
                company_website=data.company_website,
            )

            self.recruiter_repo.create(profile)

            self.db.commit()

            self.db.refresh(user)

            return user

        except Exception:
            self.db.rollback()
            raise