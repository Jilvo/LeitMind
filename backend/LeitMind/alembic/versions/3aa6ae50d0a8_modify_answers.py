"""modify answers

Revision ID: 3aa6ae50d0a8
Revises: f288e56ea0ce
Create Date: 2024-12-30 16:30:39.751123

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3aa6ae50d0a8"
down_revision: Union[str, None] = "f288e56ea0ce"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("answers", sa.Column("is_correct", sa.Boolean(), nullable=False))
    op.drop_constraint("questions_correct_answer_id_fkey", "questions", type_="foreignkey")
    op.drop_column("questions", "correct_answer_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "questions",
        sa.Column("correct_answer_id", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.create_foreign_key(
        "questions_correct_answer_id_fkey",
        "questions",
        "answers",
        ["correct_answer_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.drop_column("answers", "is_correct")
    # ### end Alembic commands ###
