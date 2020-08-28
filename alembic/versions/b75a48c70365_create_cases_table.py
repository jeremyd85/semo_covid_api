"""create cases table

Revision ID: b75a48c70365
Revises: 
Create Date: 2020-08-27 09:18:37.153116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b75a48c70365'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'cases',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('employee_case_count', sa.Integer),
        sa.Column('student_case_count', sa.Integer)
    )


def downgrade():
    pass
