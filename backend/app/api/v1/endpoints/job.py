from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from app.schemas.application import (
    ApplyJobRequest,
    ApplyJobResponse,
)

from app.services.application_service import (
    ApplicationService,
)

from app.database.session import get_db
from app.models.user import User
from app.schemas.job import (
    JobCreateRequest,
    JobResponse,
    JobUpdateRequest,
)
from app.security.dependencies import (
    require_candidate,
    require_recruiter,
)
from app.services.job_service import JobService

router = APIRouter(
    prefix="/api/v1/jobs",
    tags=["Jobs"],
)

# --------------------------------------------------
# Browse Public Jobs (Candidate)
# --------------------------------------------------

@router.get(
    "/public",
    response_model=list[JobResponse],
)
def browse_jobs(
    current_user: User = Depends(
        require_candidate,
    ),
    db: Session = Depends(get_db),
):

    service = JobService(db)

    return service.get_public_jobs()

# --------------------------------------------------
# Apply Job
# --------------------------------------------------

@router.post(
    "/{job_id}/apply",
    response_model=ApplyJobResponse,
    status_code=status.HTTP_201_CREATED,
)
def apply_job(
    job_id: int,
    request: ApplyJobRequest,
    current_user: User = Depends(
        require_candidate,
    ),
    db: Session = Depends(get_db),
):

    service = ApplicationService(db)

    return service.apply_to_job(
        job_id=job_id,
        candidate_id=current_user.id,
        resume_id=request.resume_id,
    )
# --------------------------------------------------
# Create Job
# --------------------------------------------------
@router.post(
    "",
    response_model=JobResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_job(
    data: JobCreateRequest,
    current_user: User = Depends(require_recruiter),
    db: Session = Depends(get_db),
):
    service = JobService(db)

    return service.create_job(
        recruiter_id=current_user.id,
        data=data,
    )


# --------------------------------------------------
# Get My Jobs
# --------------------------------------------------
@router.get(
    "",
    response_model=list[JobResponse],
)
def get_my_jobs(
    current_user: User = Depends(require_recruiter),
    db: Session = Depends(get_db),
):
    service = JobService(db)

    return service.get_jobs(
        recruiter_id=current_user.id,
    )

# --------------------------------------------------
# Get Single Job
# --------------------------------------------------
@router.get(
    "/{job_id}",
    response_model=JobResponse,
)
def get_job(
    job_id: int,
    current_user: User = Depends(require_recruiter),
    db: Session = Depends(get_db),
):
    service = JobService(db)

    return service.get_job(
        job_id=job_id,
        recruiter_id=current_user.id,
    )


# --------------------------------------------------
# Update Job
# --------------------------------------------------
@router.put(
    "/{job_id}",
    response_model=JobResponse,
)
def update_job(
    job_id: int,
    data: JobUpdateRequest,
    current_user: User = Depends(require_recruiter),
    db: Session = Depends(get_db),
):
    service = JobService(db)

    return service.update_job(
        job_id=job_id,
        recruiter_id=current_user.id,
        data=data,
    )


# --------------------------------------------------
# Delete Job
# --------------------------------------------------
@router.delete(
    "/{job_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_job(
    job_id: int,
    current_user: User = Depends(require_recruiter),
    db: Session = Depends(get_db),
):
    service = JobService(db)

    service.delete_job(
        job_id=job_id,
        recruiter_id=current_user.id,
    )

    return Response(status_code=status.HTTP_204_NO_CONTENT)