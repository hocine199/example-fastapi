"""add content col to post table

Revision ID: 6bbb8fc9e024
Revises: be24b246f123
Create Date: 2023-09-16 12:47:01.496869

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6bbb8fc9e024'
down_revision: Union[str, None] = 'be24b246f123'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
