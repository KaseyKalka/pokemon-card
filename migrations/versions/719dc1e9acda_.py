"""empty message

Revision ID: 719dc1e9acda
Revises: c6681879ea96
Create Date: 2023-05-31 20:53:31.260755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '719dc1e9acda'
down_revision = 'c6681879ea96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pokemon_name', sa.String(), nullable=False),
    sa.Column('ability', sa.String(), nullable=False),
    sa.Column('hp', sa.Integer(), nullable=False),
    sa.Column('defense', sa.Integer(), nullable=False),
    sa.Column('attack', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemon')
    # ### end Alembic commands ###
