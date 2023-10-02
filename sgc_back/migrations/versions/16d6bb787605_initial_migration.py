"""Initial migration.

Revision ID: 16d6bb787605
Revises: b5b45f60d5a4
Create Date: 2023-10-02 10:50:30.860448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16d6bb787605'
down_revision = 'b5b45f60d5a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cl_tcliente', schema=None) as batch_op:
        batch_op.add_column(sa.Column('clnte_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('clnte_tpidentif_id', sa.String(length=30), nullable=False))
        batch_op.add_column(sa.Column('clnte_nroident', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('clnte_estado', sa.String(length=10), nullable=False))
        batch_op.create_unique_constraint('uq_clnte_tpidentif_nroident', ['clnte_tpidentif_id', 'clnte_nroident'])
        batch_op.create_foreign_key(None, 'ge_ttipodocumento', ['clnte_tpidentif_id'], ['tdoc_documento'])
        batch_op.drop_column('cliente_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cl_tcliente', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cliente_id', sa.INTEGER(), nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint('uq_clnte_tpidentif_nroident', type_='unique')
        batch_op.drop_column('clnte_estado')
        batch_op.drop_column('clnte_nroident')
        batch_op.drop_column('clnte_tpidentif_id')
        batch_op.drop_column('clnte_id')

    # ### end Alembic commands ###