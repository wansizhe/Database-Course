"""empty message

Revision ID: 35ae7afe8db3
Revises: 5ae21fd2f5b6
Create Date: 2018-01-15 14:08:04.083756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35ae7afe8db3'
down_revision = '5ae21fd2f5b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reports',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('flag', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('comt_id', sa.Integer(), nullable=False),
    sa.Column('handle', sa.Integer(), nullable=False),
    sa.Column('report_time', sa.DateTime(), nullable=False),
    sa.Column('handle_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['comt_id'], ['comments.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reports')
    # ### end Alembic commands ###