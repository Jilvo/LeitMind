from domains.base import Base
from sqlalchemy import TIMESTAMP, CheckConstraint, Column, ForeignKey, Integer, String
from sqlalchemy.sql import func


class Progress(Base):
    __tablename__ = "progress"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    user_id = Column(
        Integer,
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    question_id = Column(
        Integer,
        ForeignKey(
            "questions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    status = Column(
        String(20),
        nullable=False,
    )
    next_review = Column(TIMESTAMP)
    attempts = Column(
        Integer,
        default=0,
    )
    created_at = Column(
        TIMESTAMP,
        server_default=func.now(),
    )
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now(),
    )

    __table_args__ = (
        CheckConstraint(
            status.in_(
                [
                    "completed",
                    "pending",
                    "in_progress",
                ]
            ),
            name="check_status",
        ),
    )
