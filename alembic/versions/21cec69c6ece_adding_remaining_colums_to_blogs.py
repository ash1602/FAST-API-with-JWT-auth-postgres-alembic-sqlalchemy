"""adding remaining colums to blogs

Revision ID: 21cec69c6ece
Revises: 5515f3d1ebce
Create Date: 2022-01-04 18:43:56.086122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21cec69c6ece'
down_revision = '5515f3d1ebce'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('blog', sa.Column('published', sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column('blog', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")
    ),)
    pass


def downgrade():
    op.drop_column('blog', 'published'),
    op.drop_column('blog', 'created_at')
    pass

