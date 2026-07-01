from fastapi import APIRouter, status

from app.schemas.search import (
    CandidateSearchRequest,
    CandidateSearchResponse,
)
from app.services.semantic_search_service import (
    SemanticSearchService,
)

router = APIRouter(
    prefix="/api/v1/search",
    tags=["Semantic Search"],
)


@router.post(
    "/candidates",
    response_model=CandidateSearchResponse,
    status_code=status.HTTP_200_OK,
)
def search_candidates(
    request: CandidateSearchRequest,
):
    """
    Search candidates using semantic similarity.

    This endpoint accepts any natural language query
    (typically a Job Description) and returns the
    most semantically similar candidates.
    """

    service = SemanticSearchService()

    return service.search(request)