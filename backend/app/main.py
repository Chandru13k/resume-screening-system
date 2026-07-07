from fastapi import FastAPI

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.job import router as job_router
from app.api.v1.endpoints.resume import router as resume_router
from app.api.v1.endpoints.matching import router as matching_router

from app.api.v1.endpoints.ranking import router as ranking_router
from app.api.v1.endpoints.dashboard import router as dashboard_router
from app.api.v1.endpoints.job_analytics import router as job_analytics_router

from app.api.v1.endpoints.candidate_dashboard import (
    router as candidate_dashboard_router,
)

from app.api.v1.endpoints.recommendation import (
    router as recommendation_router,
)

from app.api.v1.endpoints.application import (
    router as application_router,
)

from app.api.v1.endpoints.application_ranking import (
    router as application_ranking_router,
)

from app.api.v1.endpoints.recruiter_job_dashboard import (
    router as recruiter_job_dashboard_router,
)

from app.api.v1.endpoints.application_ai import (
    router as application_ai_router,
)

app = FastAPI(
    title="Resume Screening System API",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(job_router)
app.include_router(resume_router)
app.include_router(matching_router)
app.include_router(ranking_router)
app.include_router(dashboard_router)
app.include_router(job_analytics_router)
app.include_router(candidate_dashboard_router)
app.include_router(recommendation_router)
app.include_router(application_ranking_router)
app.include_router(
    recruiter_job_dashboard_router
)
app.include_router(
    application_ai_router,
)

# -------------------------
# Applications
# -------------------------
app.include_router(application_router)


@app.get("/")
def root():
    return {
        "message": "Resume Screening System API Running 🚀"
    }