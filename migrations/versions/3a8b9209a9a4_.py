"""empty message

Revision ID: 3a8b9209a9a4
Revises: 
Create Date: 2020-06-06 21:15:59.617358

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3a8b9209a9a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('visibility', sa.Boolean(), nullable=False))
    op.drop_column('event', 'visbility')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('visbility', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.drop_column('event', 'visibility')
    # ### end Alembic commands ###
