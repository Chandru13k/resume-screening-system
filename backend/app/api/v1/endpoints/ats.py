from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.ats import (
    ATSRequest,
    ATSResponse,
)
from app.services.ats_service import ATSService

router = APIRouter(
    prefix="/api/v1/ats",
    tags=["ATS Engine"],
)


@router.post(
    "/evaluate",
    response_model=ATSResponse,
    status_code=status.HTTP_200_OK,
)
def evaluate_candidates(
    request: ATSRequest,
    db: Session = Depends(get_db),
):
    """
    Evaluate candidates for a Job Description.

    This endpoint combines:
    - Semantic Search
    - Skill Matching
    - ATS Score Calculation
    """

    service = ATSService(db)

    return service.evaluate(request)