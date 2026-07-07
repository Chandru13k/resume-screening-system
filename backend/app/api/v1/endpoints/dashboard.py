from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.schemas.dashboard import DashboardResponse
from app.security.dependencies import require_recruiter
from app.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/stats",
    response_model=DashboardResponse,
)
def dashboard(
    current_user: User = Depends(
        require_recruiter
    ),
    db: Session = Depends(
        get_db
    ),
):

    service = DashboardService(db)

    return service.recruiter_dashboard(
        recruiter_id=current_user.id
    )