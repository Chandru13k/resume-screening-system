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
    TokenResponse,
)
from app.security.jwt import create_access_token
from app.security.password import hash_password, verify_password


class AuthService:

    def __init__(self, db: Session):
        self.db = db

        self.user_repo = UserRepository(db)
        self.candidate_repo = CandidateRepository(db)
        self.recruiter_repo = RecruiterRepository(db)

    # --------------------------------------------------
    # Private Helper
    # --------------------------------------------------
    def _create_user(
        self,
        email: str,
        password: str,
        role: UserRole,
    ) -> User:

        existing = self.user_repo.get_by_email(email)

        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered.",
            )

        user = User(
            email=email,
            password_hash=hash_password(password),
            role=role,
        )

        self.user_repo.create(user)

        return user

    # --------------------------------------------------
    # Candidate Registration
    # --------------------------------------------------
    def register_candidate(
        self,
        data: CandidateRegisterRequest,
    ) -> User:

        try:

            user = self._create_user(
                email=data.email,
                password=data.password,
                role=UserRole.CANDIDATE,
            )

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

    # --------------------------------------------------
    # Recruiter Registration
    # --------------------------------------------------
    def register_recruiter(
        self,
        data: RecruiterRegisterRequest,
    ) -> User:

        try:

            user = self._create_user(
                email=data.email,
                password=data.password,
                role=UserRole.RECRUITER,
            )

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

# --------------------------------------------------
# Login
# --------------------------------------------------
    def login(
        self,
        email: str,
        password: str,
    ) -> TokenResponse:

        user = self.user_repo.get_by_email(email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        access_token = create_access_token(
            {
                "sub": user.email,
                "uid": user.id,
                "role": user.role,
            }
        )

        return TokenResponse(
            access_token=access_token,
            token_type="bearer",
        )