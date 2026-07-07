from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CandidateProfileResponse(BaseModel):

    full_name: str

    phone: str | None

    location: str | None

    github_url: str | None

    linkedin_url: str | None

    portfolio_url: str | None

    model_config = ConfigDict(from_attributes=True)


class ResumeResponse(BaseModel):

    id: int

    original_filename: str

    parsing_completed: bool

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CandidateDashboardResponse(BaseModel):

    profile: CandidateProfileResponse

    resumes: list[ResumeResponse]