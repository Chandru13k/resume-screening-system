from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.schemas.matching import JobMatchResponse
from app.security.dependencies import require_recruiter
from app.services.matching_service import MatchingService

router = APIRouter(
    prefix="/api/v1/matching",
    tags=["Matching"],
)


@router.post(
    "/jobs/{job_id}",
    response_model=JobMatchResponse,
)
def match_candidates(
    job_id: int,
    current_user: User = Depends(require_recruiter),
    db: Session = Depends(get_db),
):

    service = MatchingService(db)

    try:

        return service.match_candidates(job_id)

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e),
        )