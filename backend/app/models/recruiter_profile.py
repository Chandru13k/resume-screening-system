from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin


class RecruiterProfile(Base, TimestampMixin):

    __tablename__ = "recruiter_profiles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    recruiter_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    company_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    designation: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    company_website: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    user = relationship(
        "User",
        back_populates="recruiter_profile"
    )