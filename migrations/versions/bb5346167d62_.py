"""empty message

Revision ID: bb5346167d62
Revises: 52ad1c22d8cd
Create Date: 2023-06-04 12:58:35.289461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb5346167d62'
down_revision = '52ad1c22d8cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pokemon', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_caught', sa.Boolean(), nullable=True))
        batch_op.create_unique_constraint(None, ['pokemon_name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pokemon', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('is_caught')

    # ### end Alembic commands ###