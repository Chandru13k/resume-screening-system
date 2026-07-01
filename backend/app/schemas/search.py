from pydantic import BaseModel, Field


class CandidateSearchRequest(BaseModel):
    """
    Request schema for semantic candidate search.
    """

    query: str = Field(
        ...,
        min_length=5,
        description="Job description or search query",
    )

    limit: int = Field(
        default=10,
        ge=1,
        le=50,
    )


class CandidateSearchResult(BaseModel):
    """
    Single search result.
    """

    candidate_id: int

    resume_document_id: int

    full_name: str | None

    email: str | None

    location: str | None

    skills: list[str]

    similarity_score: float


class CandidateSearchResponse(BaseModel):
    """
    Semantic search response.
    """

    candidates: list[CandidateSearchResult]