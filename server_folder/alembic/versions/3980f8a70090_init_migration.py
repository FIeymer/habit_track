"""Init migration

Revision ID: 3980f8a70090
Revises: 
Create Date: 2025-01-11 08:21:48.469713

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '3980f8a70090'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('habits')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.INTEGER(), server_default=sa.text("nextval('user_user_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('language', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('user_id', name='user_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('habits',
    sa.Column('habit_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('habit_title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('today_status', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('days_count', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('reminder', postgresql.TIME(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], name='habits_user_id_fkey'),
    sa.PrimaryKeyConstraint('habit_id', name='habits_pkey')
    )
    # ### end Alembic commands ###