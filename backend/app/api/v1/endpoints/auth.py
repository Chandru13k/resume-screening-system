from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.auth import (
    CandidateRegisterRequest,
    RecruiterRegisterRequest,
    UserResponse,
)
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"],
)


# -------------------------
# Candidate Registration
# -------------------------
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


# -------------------------
# Recruiter Registration
# -------------------------
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