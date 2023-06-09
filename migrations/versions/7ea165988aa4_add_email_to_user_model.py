"""add email field to user model

Revision ID: 7ea165988aa4
Revises: 3116a983d319
Create Date: 2023-04-27 23:53:06.089337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ea165988aa4'
down_revision = '3116a983d319'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=255), server_default='', nullable=False))
        sa.UniqueConstraint('email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('email')

    # ### end Alembic commands ###
