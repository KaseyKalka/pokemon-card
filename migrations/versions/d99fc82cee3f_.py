"""empty message

Revision ID: d99fc82cee3f
Revises: bb5346167d62
Create Date: 2023-06-04 13:12:18.871957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd99fc82cee3f'
down_revision = 'bb5346167d62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pokemon', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img_url', sa.String(), nullable=False))
        batch_op.drop_constraint('pokemon_user_id_fkey', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pokemon', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('pokemon_user_id_fkey', 'user', ['user_id'], ['id'])
        batch_op.drop_column('img_url')

    # ### end Alembic commands ###