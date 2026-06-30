from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session


from app.security.dependencies import get_current_user
from app.models.user import User
from fastapi.security import OAuth2PasswordRequestForm

from app.database.session import get_db
from app.schemas.auth import (
    CandidateRegisterRequest,
    RecruiterRegisterRequest,
    UserResponse,
    TokenResponse,
)
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"],
)


# --------------------------------------------------
# Candidate Registration
# --------------------------------------------------
@router.post(
    "/register/candidate",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_candidate(
    data: CandidateRegisterRequest,
    db: Session = Depends(get_db),
):

    service = AuthService(db)

    return service.register_candidate(data)


# --------------------------------------------------
# Recruiter Registration
# --------------------------------------------------
@router.post(
    "/register/recruiter",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_recruiter(
    data: RecruiterRegisterRequest,
    db: Session = Depends(get_db),
):

    service = AuthService(db)

    return service.register_recruiter(data)


# --------------------------------------------------
# Login
# --------------------------------------------------
@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):

    service = AuthService(db)

    return service.login(
        email=form_data.username,
        password=form_data.password,
    )
# --------------------------------------------------
# Current User
# --------------------------------------------------
@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user: User = Depends(get_current_user),
):

    return current_user