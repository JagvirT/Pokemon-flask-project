"""empty message

Revision ID: 96f1d56151e7
Revises: e75a32affd63
Create Date: 2022-12-03 17:15:29.696585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96f1d56151e7'
down_revision = 'e75a32affd63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('img_url', sa.String(), nullable=False),
    sa.Column('caption', sa.String(length=400), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###