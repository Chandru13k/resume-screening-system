from fastapi import (
    APIRouter,
    Depends,
    File,
    Response,
    UploadFile,
    status,
)
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.schemas.resume import (
    ResumeDetailsResponse,
    ResumeUploadResponse,
)
from app.security.dependencies import require_candidate
from app.services.resume_service import ResumeService

router = APIRouter(
    prefix="/api/v1/resumes",
    tags=["Resume"],
)


# --------------------------------------------------
# Upload Resume
# --------------------------------------------------

@router.post(
    "/upload",
    response_model=ResumeUploadResponse,
    status_code=status.HTTP_201_CREATED,
)
def upload_resume(
    file: UploadFile = File(...),
    current_user: User = Depends(require_candidate),
    db: Session = Depends(get_db),
):

    service = ResumeService(db)

    return service.upload_resume(
        candidate_id=current_user.id,
        file=file,
    )


# --------------------------------------------------
# Get My Resumes
# --------------------------------------------------

@router.get(
    "",
    response_model=list[ResumeUploadResponse],
)
def get_my_resumes(
    current_user: User = Depends(require_candidate),
    db: Session = Depends(get_db),
):

    service = ResumeService(db)

    return service.get_candidate_resumes(
        current_user.id,
    )


# --------------------------------------------------
# Get Resume
# --------------------------------------------------

@router.get(
    "/{resume_id}",
    response_model=ResumeDetailsResponse,
)
def get_resume(
    resume_id: int,
    current_user: User = Depends(require_candidate),
    db: Session = Depends(get_db),
):

    service = ResumeService(db)

    return service.get_resume(
        resume_id,
        current_user.id,
    )


# --------------------------------------------------
# Delete Resume
# --------------------------------------------------

@router.delete(
    "/{resume_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_resume(
    resume_id: int,
    current_user: User = Depends(require_candidate),
    db: Session = Depends(get_db),
):

    service = ResumeService(db)

    service.delete_resume(
        resume_id,
        current_user.id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )