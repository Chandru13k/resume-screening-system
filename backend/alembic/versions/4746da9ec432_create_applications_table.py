"""create applications table

Revision ID: 4746da9ec432
Revises: fa028dce51f2
Create Date: 2026-07-02 13:00:07.437877

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4746da9ec432"
down_revision: Union[str, Sequence[str], None] = "fa028dce51f2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "applications",

        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "job_id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "candidate_id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "resume_id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "status",
            sa.Enum(
                "APPLIED",
                "SHORTLISTED",
                "INTERVIEW",
                "REJECTED",
                "HIRED",
                name="applicationstatus",
            ),
            nullable=False,
        ),

        sa.Column(
            "applied_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),

        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),

        sa.ForeignKeyConstraint(
            ["candidate_id"],
            ["users.id"],
            ondelete="CASCADE",
        ),

        sa.ForeignKeyConstraint(
            ["job_id"],
            ["jobs.id"],
            ondelete="CASCADE",
        ),

        sa.ForeignKeyConstraint(
            ["resume_id"],
            ["resume_documents.id"],
            ondelete="CASCADE",
        ),

        sa.UniqueConstraint(
            "job_id",
            "candidate_id",
            name="uq_job_candidate",
        ),

        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        op.f("ix_applications_candidate_id"),
        "applications",
        ["candidate_id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_applications_id"),
        "applications",
        ["id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_applications_job_id"),
        "applications",
        ["job_id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_applications_resume_id"),
        "applications",
        ["resume_id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        op.f("ix_applications_resume_id"),
        table_name="applications",
    )

    op.drop_index(
        op.f("ix_applications_job_id"),
        table_name="applications",
    )

    op.drop_index(
        op.f("ix_applications_id"),
        table_name="applications",
    )

    op.drop_index(
        op.f("ix_applications_candidate_id"),
        table_name="applications",
    )

    op.drop_table("applications")

    op.execute("DROP TYPE IF EXISTS applicationstatus")