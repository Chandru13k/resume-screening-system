from datetime import datetime

from pydantic import BaseModel

from app.enums.application_status import ApplicationStatus


# ---------------------------------------
# Apply
# ---------------------------------------

class ApplyJobRequest(BaseModel):

    resume_id: int


class ApplyJobResponse(BaseModel):

    application_id: int

    status: ApplicationStatus

    message: str


# ---------------------------------------
# Candidate Dashboard
# ---------------------------------------

class CandidateApplicationResponse(BaseModel):

    application_id: int

    job_id: int

    job_title: str

    company_name: str

    location: str | None

    status: ApplicationStatus

    applied_at: datetime


# ---------------------------------------
# Recruiter Dashboard
# ---------------------------------------

class RecruiterApplicationResponse(BaseModel):

    application_id: int

    candidate_id: int

    candidate_name: str

    candidate_email: str

    resume_id: int

    status: ApplicationStatus

    applied_at: datetime


# ---------------------------------------
# Update Status
# ---------------------------------------

class UpdateApplicationStatusRequest(BaseModel):

    status: ApplicationStatus