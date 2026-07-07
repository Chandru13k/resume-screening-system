from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.enums.application_status import ApplicationStatus


class Application(Base):

    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    job_id: Mapped[int] = mapped_column(
        ForeignKey(
            "jobs.id",
            ondelete="CASCADE",
        ),
        index=True,
    )

    candidate_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        index=True,
    )

    resume_id: Mapped[int] = mapped_column(
        ForeignKey(
            "resume_documents.id",
            ondelete="CASCADE",
        ),
        index=True,
    )

    status: Mapped[ApplicationStatus] = mapped_column(
        Enum(ApplicationStatus),
        default=ApplicationStatus.APPLIED,
        nullable=False,
    )

    applied_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    job = relationship(
        "Job",
        back_populates="applications",
    )

    candidate = relationship(
        "User",
        back_populates="applications",
)

    resume = relationship(
        "ResumeDocument",
        back_populates="applications",
    )
    ai_insight = relationship(
        "ApplicationAIInsight",
        back_populates="application",
        uselist=False,
        cascade="all, delete-orphan",
    )