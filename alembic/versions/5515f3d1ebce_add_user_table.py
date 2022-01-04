"""add user table

Revision ID: 5515f3d1ebce
Revises: 2ab6c73c05c9
Create Date: 2022-01-04 18:31:50.601071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5515f3d1ebce'
down_revision = '2ab6c73c05c9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
