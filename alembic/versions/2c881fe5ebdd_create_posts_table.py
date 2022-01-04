"""create posts table

Revision ID: 2c881fe5ebdd
Revises: 
Create Date: 2022-01-04 18:08:42.193312

"""
from alembic import op
import sqlalchemy as sa

from app.models import Blog


# revision identifiers, used by Alembic.
revision = '2c881fe5ebdd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('blog', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title',sa.String(), nullable=False))
    


def downgrade():
    pass
