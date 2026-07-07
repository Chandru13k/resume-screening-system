from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.ai.hybrid_matcher import HybridMatcher
from app.database.session import get_db
from app.repositories.job_repository import JobRepository
from app.schemas.ranking import RankingResponse
from app.security.dependencies import require_recruiter

router = APIRouter(
    prefix="/api/v1/ranking",
    tags=["Ranking"],
)


@router.get(
    "/jobs/{job_id}",
    response_model=RankingResponse,
)
def get_ranking(
    job_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_recruiter),
):

    job = JobRepository(db).get_by_id(job_id)

    if not job:

        raise HTTPException(
            status_code=404,
            detail="Job not found.",
        )

    matcher = HybridMatcher(db)

    return {

        "candidates": matcher.rank_candidates(job)

    }