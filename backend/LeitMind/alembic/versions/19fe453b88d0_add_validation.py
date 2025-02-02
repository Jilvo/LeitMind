"""add_validation

Revision ID: 19fe453b88d0
Revises: b17f616f8e45
Create Date: 2025-02-02 14:16:12.737426

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "19fe453b88d0"
down_revision: Union[str, None] = "b17f616f8e45"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("attempts", sa.Column("answer_id", sa.Integer(), nullable=False))
    op.add_column("attempts", sa.Column("attempt_count", sa.Integer(), nullable=False))
    op.add_column("attempts", sa.Column("leitner_box", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "attempts", "answers", ["answer_id"], ["id"], ondelete="CASCADE")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "attempts", type_="foreignkey")
    op.drop_column("attempts", "leitner_box")
    op.drop_column("attempts", "attempt_count")
    op.drop_column("attempts", "answer_id")
    # ### end Alembic commands ###
