"""add column Created_at to users table

Revision ID: 78108d266482
Revises: dc726d9f76f0
Create Date: 2023-09-16 13:06:20.916888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '78108d266482'
down_revision: Union[str, None] = 'dc726d9f76f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('users', 'created_at')
    pass
