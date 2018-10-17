"""empty message

Revision ID: fa91070a5149
Revises: 35ae7afe8db3
Create Date: 2018-01-15 15:54:25.551636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa91070a5149'
down_revision = '35ae7afe8db3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reports', sa.Column('admin_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'reports', 'users', ['admin_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reports', type_='foreignkey')
    op.drop_column('reports', 'admin_id')
    # ### end Alembic commands ###
