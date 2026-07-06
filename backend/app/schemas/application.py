from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.enums.application_status import ApplicationStatus


class ApplyJobRequest(BaseModel):
    resume_id: int


class ApplyJobResponse(BaseModel):
    application_id: int
    status: ApplicationStatus
    message: str


class CandidateApplicationResponse(BaseModel):
    application_id: int
    job_id: int
    job_title: str
    company_name: str
    location: str | None
    status: ApplicationStatus
    applied_at: datetime


class RecruiterApplicationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    application_id: int
    candidate_id: int
    candidate_name: str
    candidate_email: str
    resume_id: int
    status: ApplicationStatus
    applied_at: datetime


class UpdateApplicationStatusRequest(BaseModel):
    status: ApplicationStatus


class UpdateApplicationStatusResponse(BaseModel):
    application_id: int
    status: ApplicationStatus
    message: str