"""create_application_ai_insights_table

Revision ID: c95da19c5910
Revises: 4746da9ec432
Create Date: 2026-07-07 11:04:01.976295

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "c95da19c5910"
down_revision: Union[str, Sequence[str], None] = "4746da9ec432"
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table(
        "application_ai_insights",

        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "application_id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "summary",
            sa.Text(),
            nullable=False,
        ),

        sa.Column(
            "strengths",
            sa.Text(),
            nullable=False,
        ),

        sa.Column(
            "weaknesses",
            sa.Text(),
            nullable=False,
        ),

        sa.Column(
            "score_explanation",
            sa.Text(),
            nullable=False,
        ),

        sa.Column(
            "interview_questions",
            sa.Text(),
            nullable=False,
        ),

        sa.Column(
            "recommendation",
            sa.Text(),
            nullable=False,
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),

        sa.ForeignKeyConstraint(
            ["application_id"],
            ["applications.id"],
            ondelete="CASCADE",
        ),

        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_application_ai_insights_application_id",
        "application_ai_insights",
        ["application_id"],
        unique=True,
    )

    op.create_index(
        "ix_application_ai_insights_id",
        "application_ai_insights",
        ["id"],
        unique=False,
    )


def downgrade() -> None:

    op.drop_index(
        "ix_application_ai_insights_id",
        table_name="application_ai_insights",
    )

    op.drop_index(
        "ix_application_ai_insights_application_id",
        table_name="application_ai_insights",
    )

    op.drop_table(
        "application_ai_insights"
    )