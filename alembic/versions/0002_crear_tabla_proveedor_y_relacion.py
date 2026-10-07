"""crear tabla proveedor y relacion foreign key en libro

Revision ID: 0002
Revises: 0001
Create Date: 2026-10-07 11:37:30.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '0002'
down_revision: Union[str, None] = '0001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Crear tabla proveedor
    op.create_table(
        'proveedor',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nombre_proveedor', sa.String(length=100), nullable=False),
        sa.Column('telefono_proveedor', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_proveedor_nombre_proveedor'), 'proveedor', ['nombre_proveedor'], unique=False)

    # 2. Agregar columna proveedor_id y Foreign Key en tabla libro usando batch_alter_table (compatible con SQLite)
    with op.batch_alter_table('libro', schema=None) as batch_op:
        batch_op.add_column(sa.Column('proveedor_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_libro_proveedor', 'proveedor', ['proveedor_id'], ['id'])


def downgrade() -> None:
    with op.batch_alter_table('libro', schema=None) as batch_op:
        batch_op.drop_constraint('fk_libro_proveedor', type_='foreignkey')
        batch_op.drop_column('proveedor_id')

    op.drop_index(op.f('ix_proveedor_nombre_proveedor'), table_name='proveedor')
    op.drop_table('proveedor')
