from datetime import datetime

from pydantic import BaseModel


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

    class Config:

        from_attributes = True


class DashboardResponse(BaseModel):

    stats: DashboardStats

    recent_jobs: list[RecentJob]