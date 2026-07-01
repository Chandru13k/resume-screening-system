from fastapi import FastAPI

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.resume import router as resume_router
from app.api.v1.endpoints.resume_profile import router as resume_profile_router
from app.api.v1.endpoints.search import router as search_router
from app.api.v1.endpoints.ats import router as ats_router
app = FastAPI(
    title="Resume Screening System",
    version="1.0.0",
)
app.include_router(ats_router)

app.include_router(auth_router)
app.include_router(resume_router)
app.include_router(resume_profile_router)
app.include_router(search_router)


@app.get("/")
def root():
    return {
        "message": "Resume Screening System API"
    }