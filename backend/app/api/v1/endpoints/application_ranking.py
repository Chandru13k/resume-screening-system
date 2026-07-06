from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.security.dependencies import require_recruiter

from app.services.application_ranking_service import (
    ApplicationRankingService,
)

router = APIRouter(
    prefix="/api/v1/application-ranking",
    tags=["Application Ranking"],
)


# --------------------------------------------------
# Rank Applicants
# --------------------------------------------------

@router.get(
    "/jobs/{job_id}",
)
def rank_job_applicants(
    job_id: int,
    current_user: User = Depends(
        require_recruiter,
    ),
    db: Session = Depends(get_db),
):

    service = ApplicationRankingService(db)

    return service.rank_applicants(
        recruiter_id=current_user.id,
        job_id=job_id,
    )