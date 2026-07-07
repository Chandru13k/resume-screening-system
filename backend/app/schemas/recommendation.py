from pydantic import BaseModel


class RecommendedJob(BaseModel):

    job_id: int

    title: str

    company_name: str

    location: str | None

    overall_score: float


class RecommendationResponse(BaseModel):

    recommendations: list[RecommendedJob]