from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DashboardStats(BaseModel):

    total_jobs: int

    active_jobs: int

    parsed_resumes: int


class RecentJob(BaseModel):

    id: int

    title: str

    company_name: str

    status: str

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class DashboardResponse(BaseModel):

    stats: DashboardStats

    recent_jobs: list[RecentJob]