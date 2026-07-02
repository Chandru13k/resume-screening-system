from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.schemas.job_analytics import JobAnalyticsResponse
from app.security.dependencies import require_recruiter
from app.services.job_analytics_service import JobAnalyticsService

router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/job/{job_id}",
    response_model=JobAnalyticsResponse,
)
def analytics(
    job_id: int,
    current_user: User = Depends(require_recruiter),
    db: Session = Depends(get_db),
):

    try:

        return JobAnalyticsService(db).analytics(
            job_id
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )