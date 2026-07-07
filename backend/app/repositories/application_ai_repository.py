from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.application_ai_insight import (
    ApplicationAIInsight,
)


class ApplicationAIRepository:

    def __init__(self, db: Session):
        self.db = db

    # -----------------------------------
    # Get by Application
    # -----------------------------------

    def get_by_application(
        self,
        application_id: int,
    ) -> ApplicationAIInsight | None:

        statement = (
            select(ApplicationAIInsight)
            .where(
                ApplicationAIInsight.application_id
                == application_id
            )
        )

        return self.db.scalar(statement)

    # -----------------------------------
    # Create
    # -----------------------------------

    def create(
        self,
        insight: ApplicationAIInsight,
    ) -> ApplicationAIInsight:

        self.db.add(insight)

        self.db.flush()

        self.db.refresh(insight)

        return insight