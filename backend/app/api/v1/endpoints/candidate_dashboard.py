from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.schemas.candidate_dashboard import (
    CandidateDashboardResponse,
)
from app.security.dependencies import require_candidate
from app.services.candidate_dashboard_service import (
    CandidateDashboardService,
)
from app.schemas.application import (
    CandidateApplicationResponse,
)
from app.services.application_service import (
    ApplicationService,
)
router = APIRouter(
    prefix="/api/v1/candidate",
    tags=["Candidate Dashboard"],
)
# --------------------------------------------------
# My Applications
# --------------------------------------------------

@router.get(
    "/applications",
    response_model=list[
        CandidateApplicationResponse
    ],
)
def get_my_applications(
    current_user: User = Depends(
        require_candidate
    ),
    db: Session = Depends(get_db),
):

    service = ApplicationService(db)

    return service.get_candidate_applications(
        current_user.id
    )

@router.get(
    "/dashboard",
    response_model=CandidateDashboardResponse,
)
def dashboard(
    current_user: User = Depends(
        require_candidate
    ),
    db: Session = Depends(
        get_db
    ),
):

    return CandidateDashboardService(
        db
    ).dashboard(
        current_user.id
    )