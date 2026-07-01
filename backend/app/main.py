from fastapi import FastAPI

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.job import router as job_router

app = FastAPI(
    title="Resume Screening System API",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(job_router)


@app.get("/")
def root():
    return {
        "message": "Resume Screening System API Running 🚀"
    }