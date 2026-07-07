from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.models.user import User

from app.schemas.application_ai import (
    ApplicationAIInsightResponse,
)

from app.security.dependencies import (
    require_recruiter,
)

from app.services.application_ai_service import (
    ApplicationAIService,
)


router = APIRouter(
    prefix="/api/v1",
    tags=["AI Insights"],
)


@router.get(
    "/applications/{application_id}/ai-insights",
    response_model=ApplicationAIInsightResponse,
)
def get_ai_insights(
    application_id: int,
    current_user: User = Depends(
        require_recruiter,
    ),
    db: Session = Depends(
        get_db,
    ),
):

    service = ApplicationAIService(
        db,
    )

    return service.get_ai_insights(
        recruiter_id=current_user.id,
        application_id=application_id,
    )