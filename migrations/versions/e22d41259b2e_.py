"""empty message

Revision ID: e22d41259b2e
Revises: 066a088c3d80
Create Date: 2020-06-05 01:36:38.023308

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e22d41259b2e'
down_revision = '066a088c3d80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('event', 'visbility',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.alter_column('user', 'admin',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'admin',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.alter_column('event', 'visbility',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    # ### end Alembic commands ###
