from fastapi import FastAPI

from app.api.v1.endpoints.auth import router as auth_router

app = FastAPI(
    title="Resume Screening System API",
    version="1.0.0"
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Resume Screening System API Running 🚀"
    }