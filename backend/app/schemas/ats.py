from pydantic import BaseModel, Field


class ATSRequest(BaseModel):
    """
    Request schema for ATS evaluation.
    """

    job_description: str = Field(
        ...,
        min_length=20,
    )

    candidate_limit: int = Field(
        default=10,
        ge=1,
        le=50,
    )


class ATSCandidate(BaseModel):

    candidate_id: int

    resume_document_id: int

    full_name: str | None

    email: str | None

    location: str | None

    semantic_score: float

    skill_match_score: float

    overall_score: float

    matched_skills: list[str]

    missing_skills: list[str]


class ATSResponse(BaseModel):

    candidates: list[ATSCandidate]