from fastapi import (
    APIRouter,
    Depends,
    File,
    UploadFile,
    status,
)
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.schemas.resume import ResumeUploadResponse
from app.security.dependencies import require_candidate
from app.services.resume_service import ResumeService

router = APIRouter(
    prefix="/api/v1/resumes",
    tags=["Resume"],
)


@router.post(
    "/upload",
    response_model=ResumeUploadResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_resume(
    file: UploadFile = File(...),
    current_user: User = Depends(require_candidate),
    db: Session = Depends(get_db),
):

    service = ResumeService(db)

    return await service.upload_resume(
        file=file,
        current_user=current_user,
    )