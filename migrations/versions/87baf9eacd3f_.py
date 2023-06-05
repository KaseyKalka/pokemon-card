"""empty message

Revision ID: 87baf9eacd3f
Revises: d99fc82cee3f
Create Date: 2023-06-04 18:31:01.062976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87baf9eacd3f'
down_revision = 'd99fc82cee3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('pokemon_name', sa.String(), nullable=False),
    sa.Column('img_url', sa.String(), nullable=False),
    sa.Column('ability', sa.String(), nullable=False),
    sa.Column('hp', sa.Integer(), nullable=False),
    sa.Column('defense', sa.Integer(), nullable=False),
    sa.Column('attack', sa.Integer(), nullable=False),
    sa.Column('is_caught', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('pokemon_name'),
    sa.UniqueConstraint('pokemon_name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('caught_pokemon',
    sa.Column('user_caught_id', sa.Integer(), nullable=True),
    sa.Column('pokemon_caught', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['pokemon_caught'], ['pokemon.pokemon_name'], ),
    sa.ForeignKeyConstraint(['user_caught_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('caught_pokemon')
    op.drop_table('user')
    op.drop_table('pokemon')
    # ### end Alembic commands ###
