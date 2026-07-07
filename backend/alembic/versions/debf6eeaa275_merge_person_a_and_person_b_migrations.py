"""merge person-a and person-b migrations

Revision ID: debf6eeaa275
Revises: 325ef1117f59, c95da19c5910
Create Date: 2026-07-07 12:20:49.681665

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'debf6eeaa275'
down_revision: Union[str, Sequence[str], None] = ('325ef1117f59', 'c95da19c5910')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
