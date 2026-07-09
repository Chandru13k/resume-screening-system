from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


# --------------------------------------------------
# Create Job
# --------------------------------------------------
class JobCreateRequest(BaseModel):
    title: str = Field(min_length=3, max_length=255)

    company_name: str

    location: str | None = None

    work_mode: str | None = None

    employment_type: str | None = None

    experience_required: str | None = None

    salary_min: Decimal | None = None

    salary_max: Decimal | None = None

    total_positions: int = Field(default=1, ge=1)

    application_deadline: date | None = None

    description: str = Field(min_length=20)


# --------------------------------------------------
# Update Job
# --------------------------------------------------
class JobUpdateRequest(BaseModel):
    title: str | None = None

    company_name: str | None = None

    location: str | None = None

    work_mode: str | None = None

    employment_type: str | None = None

    experience_required: str | None = None

    salary_min: Decimal | None = None

    salary_max: Decimal | None = None

    total_positions: int | None = Field(default=None, ge=1)

    application_deadline: date | None = None

    description: str | None = None

    status: str | None = None

    is_active: bool | None = None


# --------------------------------------------------
# Job Response
# --------------------------------------------------
class JobResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int

    recruiter_id: int

    title: str

    company_name: str

    location: str | None

    work_mode: str | None

    employment_type: str | None

    experience_required: str | None

    salary_min: Decimal | None

    salary_max: Decimal | None

    total_positions: int

    application_deadline: date | None

    description: str

    status: str

    is_active: bool

    is_applied: bool = False