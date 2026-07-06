from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.security.dependencies import require_recruiter

from app.services.recruiter_job_dashboard_service import (
    RecruiterJobDashboardService,
)

router = APIRouter(
    prefix="/api/v1/recruiter-dashboard",
    tags=["Recruiter Dashboard"],
)


# --------------------------------------------------
# Recruiter Job Dashboard
# --------------------------------------------------

@router.get(
    "/jobs/{job_id}",
)
def recruiter_job_dashboard(
    job_id: int,
    current_user: User = Depends(require_recruiter),
    db: Session = Depends(get_db),
):

    service = RecruiterJobDashboardService(db)

    return service.get_dashboard(
        recruiter_id=current_user.id,
        job_id=job_id,
    )