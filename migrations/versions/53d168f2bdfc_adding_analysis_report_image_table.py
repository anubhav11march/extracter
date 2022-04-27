"""Adding Analysis Report Image Table

Revision ID: 53d168f2bdfc
Revises: 1de1af862e18
Create Date: 2022-04-27 23:32:44.125208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53d168f2bdfc'
down_revision = '1de1af862e18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('analysis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patientId', sa.Integer(), nullable=True),
    sa.Column('pdfName', sa.String(length=80), nullable=True),
    sa.Column('analysisImgs', sa.String(length=500), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['patientId'], ['patientsusers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('analysis')
    # ### end Alembic commands ###