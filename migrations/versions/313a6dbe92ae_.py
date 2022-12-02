"""empty message

Revision ID: 313a6dbe92ae
Revises: 33760722502e
Create Date: 2022-12-02 16:51:14.631664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '313a6dbe92ae'
down_revision = '33760722502e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.alter_column('list_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.alter_column('list_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
