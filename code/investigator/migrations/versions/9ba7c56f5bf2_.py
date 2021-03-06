"""empty message

Revision ID: 9ba7c56f5bf2
Revises: 55a696eebb60
Create Date: 2016-06-16 16:20:36.298587

"""

# revision identifiers, used by Alembic.
revision = '9ba7c56f5bf2'
down_revision = '55a696eebb60'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('datum', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='data_pkey')
    )
    ### end Alembic commands ###
