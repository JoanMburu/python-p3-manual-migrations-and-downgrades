"""Renaming students to scholars

Revision ID: 18bbd724b779
Revises: 791279dd0760
Create Date: 2024-08-03 15:36:22.783154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18bbd724b779'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
