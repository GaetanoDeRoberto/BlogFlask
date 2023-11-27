"""migrazione iniziale

Revision ID: c1d299b5fea0
Revises: 
Create Date: 2023-11-28 00:03:32.188818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1d299b5fea0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('utenti', schema=None) as batch_op:
        batch_op.add_column(sa.Column('telefono', sa.Numeric(precision=10), nullable=True))
        batch_op.create_unique_constraint(None, ['telefono'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('utenti', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('telefono')

    # ### end Alembic commands ###
