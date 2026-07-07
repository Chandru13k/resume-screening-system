from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User

from app.schemas.application import (
    ApplyJobRequest,
    ApplyJobResponse,
    CandidateApplicationResponse,
    RecruiterApplicationResponse,
    UpdateApplicationStatusRequest,
    UpdateApplicationStatusResponse,
)

from app.schemas.job import JobResponse

from app.security.dependencies import (
    require_candidate,
    require_recruiter,
)

from app.services.application_service import (
    ApplicationService,
)

from app.repositories.job_repository import JobRepository


router = APIRouter(
    prefix="/api/v1",
    tags=["Applications"],
)


# --------------------------------------------------
# Candidate - Browse Jobs
# --------------------------------------------------

@router.get(
    "/candidate/jobs",
    response_model=list[JobResponse],
)
def browse_jobs(
    current_user: User = Depends(require_candidate),
    db: Session = Depends(get_db),
):

    return JobRepository(db).get_active_jobs()


# --------------------------------------------------
# Candidate - Apply
# --------------------------------------------------

@router.post(
    "/jobs/{job_id}/apply",
    response_model=ApplyJobResponse,
    status_code=status.HTTP_201_CREATED,
)
def apply_job(
    job_id: int,
    request: ApplyJobRequest,
    current_user: User = Depends(require_candidate),
    db: Session = Depends(get_db),
):

    service = ApplicationService(db)

    return service.apply_to_job(
        job_id=job_id,
        candidate_id=current_user.id,
        resume_id=request.resume_id,
    )


# --------------------------------------------------
# Candidate - My Applications
# --------------------------------------------------

@router.get(
    "/candidate/applications",
    response_model=list[CandidateApplicationResponse],
)
def get_my_applications(
    current_user: User = Depends(require_candidate),
    db: Session = Depends(get_db),
):

    service = ApplicationService(db)

    return service.get_candidate_applications(
        current_user.id,
    )


# --------------------------------------------------
# Recruiter - View Applicants
# --------------------------------------------------

@router.get(
    "/jobs/{job_id}/applications",
    response_model=list[RecruiterApplicationResponse],
)
def get_job_applications(
    job_id: int,
    current_user: User = Depends(require_recruiter),
    db: Session = Depends(get_db),
):

    service = ApplicationService(db)

    return service.get_job_applications(
        recruiter_id=current_user.id,
        job_id=job_id,
    )


# --------------------------------------------------
# Recruiter - Update Status
# --------------------------------------------------

@router.patch(
    "/applications/{application_id}/status",
    response_model=UpdateApplicationStatusResponse,
)
def update_application_status(
    application_id: int,
    request: UpdateApplicationStatusRequest,
    current_user: User = Depends(require_recruiter),
    db: Session = Depends(get_db),
):

    service = ApplicationService(db)

    return service.update_status(
        recruiter_id=current_user.id,
        application_id=application_id,
        status_value=request.status,
    )