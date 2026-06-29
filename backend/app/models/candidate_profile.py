from sqlalchemy import ForeignKey, Integer,  String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.database.base import Base
from app.database.mixins import TimestampMixin


class CandidateProfile(Base, TimestampMixin):

    __tablename__ = "candidate_profiles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    full_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    location: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True
    )

    github_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    linkedin_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    portfolio_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    coding_profiles: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True
    )

    user = relationship(
        "User",
        back_populates="candidate_profile"
    )