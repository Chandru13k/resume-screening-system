from datetime import date
from decimal import Decimal
import sqlalchemy as sa

from sqlalchemy import (
    Boolean,
    Date,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin


class Job(Base, TimestampMixin):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    recruiter_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    company_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    location: Mapped[str | None] = mapped_column(
        String(150),
    )

    work_mode: Mapped[str | None] = mapped_column(
        String(50),
    )

    employment_type: Mapped[str | None] = mapped_column(
        String(50),
    )

    experience_required: Mapped[str | None] = mapped_column(
        String(100),
    )

    salary_min: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
    )

    salary_max: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
    )

    total_positions: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    application_deadline: Mapped[date | None] = mapped_column(
        Date,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="OPEN",
        server_default="OPEN",
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default=sa.true(),
    )

    recruiter = relationship(
        "User"
    )

    applications = relationship(
        "Application",
        cascade="all, delete-orphan",
    )