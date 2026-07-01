from datetime import datetime

from pydantic import BaseModel


class ResumeProfileResponse(BaseModel):

    id: int
    resume_document_id: int

    full_name: str | None
    email: str | None
    phone: str | None
    location: str | None
    summary: str | None

    github_url: str | None
    linkedin_url: str | None
    portfolio_url: str | None

    coding_profiles: dict | None

    skills: list | None
    education: list | None
    experience: list | None
    projects: list | None
    certifications: list | None
    languages: list | None
    achievements: list | None

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True