"""create sub category and theme

Revision ID: 4df70953acaa
Revises: 11cdbc007ab5
Create Date: 2025-01-05 09:36:22.592693

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4df70953acaa"
down_revision: Union[str, None] = "11cdbc007ab5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=True),
        sa.Column("updated_at", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("username", sa.String(length=50), nullable=False),
        sa.Column("email", sa.String(length=100), nullable=False),
        sa.Column("hashed_password", sa.Text(), nullable=False),
        sa.Column("country", sa.String(length=50), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=True),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "questions",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("creator_id", sa.Integer(), nullable=True),
        sa.Column("explanation", sa.Text(), nullable=True),
        sa.Column("image_path", sa.Text(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=True),
        sa.Column("updated_at", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["category_id"], ["categories.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["creator_id"], ["users.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "sub_categories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("country", sa.String(length=2), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=True),
        sa.Column("updated_at", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["category_id"], ["categories.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "answers",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("question_id", sa.Integer(), nullable=False),
        sa.Column("is_correct", sa.Boolean(), nullable=False),
        sa.Column("text", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(["question_id"], ["questions.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "themes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("sub_category_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=True),
        sa.Column("updated_at", sa.TIMESTAMP(), server_default=sa.text("now()"), nullable=True),
        sa.ForeignKeyConstraint(["sub_category_id"], ["sub_categories.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("themes")
    op.drop_table("answers")
    op.drop_table("sub_categories")
    op.drop_table("questions")
    op.drop_table("users")
    op.drop_table("categories")
    # ### end Alembic commands ###
