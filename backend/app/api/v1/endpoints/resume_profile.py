from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.resume_document import ResumeDocument
from app.models.user import User
from app.schemas.resume_profile import ResumeProfileResponse
from app.security.dependencies import require_candidate
from app.services.resume_profile_service import ResumeProfileService

router = APIRouter(
    prefix="/api/v1/resume-profile",
    tags=["Resume Profile"],
)


@router.post(
    "/{resume_id}",
    response_model=ResumeProfileResponse,
)
def parse_resume(
    resume_id: int,
    current_user: User = Depends(require_candidate),
    db: Session = Depends(get_db),
):

    resume = db.get(
        ResumeDocument,
        resume_id,
    )

    if not resume:

        raise HTTPException(
            status_code=404,
            detail="Resume not found.",
        )

    if resume.candidate_id != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="Access denied.",
        )

    service = ResumeProfileService(db)

    return service.parse_resume(resume)