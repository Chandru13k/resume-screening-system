from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
    Text,
)

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin


class ResumeProfile(Base, TimestampMixin):

    __tablename__ = "resume_profiles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    resume_document_id: Mapped[int] = mapped_column(
        ForeignKey(
            "resume_documents.id",
            ondelete="CASCADE",
        ),
        unique=True,
        nullable=False,
        index=True,
    )

    # ---------- Basic Information ----------

    full_name: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    location: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # ---------- Professional Links ----------

    github_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    linkedin_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    portfolio_url: Mapped[str |None] = mapped_column(
        String(255),
        nullable=True,
    )

    coding_profiles: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    # ---------- Resume Sections ----------

    skills: Mapped[list | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    education: Mapped[list | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    experience: Mapped[list | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    projects: Mapped[list | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    certifications: Mapped[list | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    languages: Mapped[list | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    achievements: Mapped[list | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    resume_document = relationship(
        "ResumeDocument",
        backref="profile",
    )