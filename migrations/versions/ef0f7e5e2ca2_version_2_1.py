"""version 2.1

Revision ID: ef0f7e5e2ca2
Revises: 4b08057c25e3
Create Date: 2017-11-01 03:44:05.377473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef0f7e5e2ca2'
down_revision = '4b08057c25e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.drop_constraint('comments_pitches_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'pitches', ['pitch_id'], ['id'])
    op.drop_column('comments', 'pitches')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitches', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_pitches_fkey', 'comments', 'pitches', ['pitches'], ['id'])
    op.drop_column('comments', 'pitch_id')
    # ### end Alembic commands ###
