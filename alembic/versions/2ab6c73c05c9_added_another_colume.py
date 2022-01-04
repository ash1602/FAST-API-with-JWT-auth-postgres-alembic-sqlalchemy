"""added another colume

Revision ID: 2ab6c73c05c9
Revises: 2c881fe5ebdd
Create Date: 2022-01-04 18:22:08.764496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ab6c73c05c9'
down_revision = '2c881fe5ebdd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('blog', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('blog', 'content')
