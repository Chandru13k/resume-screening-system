from pydantic import BaseModel


class JobAnalyticsResponse(BaseModel):

    job_id: int

    job_title: str

    total_candidates: int

    average_match_score: float

    top_score: float

    recommended_for_interview: int