from domains.base import (
    Base,
)
from sqlalchemy import (
    TIMESTAMP,
    Column,
    ForeignKey,
    Integer,
    Text,
)
from sqlalchemy.sql import (
    func,
)


class Feedback(Base):
    __tablename__ = "feedback"

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
    content = Column(
        Text,
        nullable=False,
    )
    submitted_at = Column(
        TIMESTAMP,
        server_default=func.now(),
    )
