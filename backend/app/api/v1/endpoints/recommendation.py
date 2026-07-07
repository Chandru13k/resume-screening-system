from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.schemas.recommendation import RecommendationResponse
from app.security.dependencies import require_candidate
from app.services.recommendation_service import (
    RecommendationService,
)

router = APIRouter(
    prefix="/api/v1/candidate",
    tags=["Candidate Dashboard"],
)


@router.get(
    "/recommended-jobs",
    response_model=RecommendationResponse,
)
def recommended_jobs(
    current_user: User = Depends(
        require_candidate
    ),
    db: Session = Depends(get_db),
):

    return RecommendationService(
        db
    ).recommend_jobs(
        current_user.id
    )