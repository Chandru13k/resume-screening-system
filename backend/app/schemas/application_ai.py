from datetime import datetime

from pydantic import BaseModel


class ApplicationAIInsightResponse(BaseModel):

    application_id: int

    summary: str

    strengths: list[str]

    weaknesses: list[str]

    score_explanation: str

    interview_questions: list[str]

    recommendation: str

    created_at: datetime