"""Changed document content type

Revision ID: 539e86b185ee
Revises: 59b3d43d428f
Create Date: 2025-06-17 11:32:07.097757

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '539e86b185ee'
down_revision: Union[str, None] = '59b3d43d428f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('documents', 'content',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               type_=sa.Text(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('documents', 'content',
               existing_type=sa.Text(),
               type_=postgresql.JSON(astext_type=sa.Text()),
               existing_nullable=True)
    # ### end Alembic commands ###
