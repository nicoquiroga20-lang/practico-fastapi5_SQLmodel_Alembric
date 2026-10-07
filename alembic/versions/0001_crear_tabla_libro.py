"""crear tabla libro

Revision ID: 0001
Revises: 
Create Date: 2026-10-07 11:37:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '0001'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'libro',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('titulo', sa.String(length=150), nullable=False),
        sa.Column('autor', sa.String(length=100), nullable=False),
        sa.Column('precio', sa.Float(), nullable=False),
        sa.Column('disponible', sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('libro')
