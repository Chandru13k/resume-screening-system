"""add missing resume document columns

Revision ID: 31e8d1086420
Revises: debf6eeaa275
Create Date: 2026-07-07

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "31e8d1086420"
down_revision: Union[str, Sequence[str], None] = "debf6eeaa275"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add new columns as nullable
    op.add_column(
        "resume_documents",
        sa.Column("file_type", sa.String(length=20), nullable=True),
    )

    op.add_column(
        "resume_documents",
        sa.Column("file_size", sa.Integer(), nullable=True),
    )

    op.add_column(
        "resume_documents",
        sa.Column("upload_status", sa.String(length=30), nullable=True),
    )

    # Populate existing rows
    op.execute(
        """
        UPDATE resume_documents
        SET
            file_type = '.pdf',
            file_size = 0,
            upload_status = 'uploaded'
        WHERE file_type IS NULL
        """
    )

    # Make columns non-nullable
    op.alter_column(
        "resume_documents",
        "file_type",
        nullable=False,
    )

    op.alter_column(
        "resume_documents",
        "file_size",
        nullable=False,
    )

    op.alter_column(
        "resume_documents",
        "upload_status",
        nullable=False,
    )


def downgrade() -> None:
    op.drop_column("resume_documents", "upload_status")
    op.drop_column("resume_documents", "file_size")
    op.drop_column("resume_documents", "file_type")