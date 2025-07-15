from domains.base import Base
from sqlalchemy import TIMESTAMP, Column, Date, ForeignKey, Integer
from sqlalchemy.sql import func


class LeaderboardHistory(Base):
    __tablename__ = "leaderboard_history"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    period_start = Column(
        Date,
        nullable=False,
    )
    period_end = Column(
        Date,
        nullable=False,
    )
    rank = Column(
        Integer,
        nullable=False,
    )
    user_id = Column(
        Integer,
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    score = Column(
        Integer,
        nullable=False,
    )
    created_at = Column(
        TIMESTAMP,
        server_default=func.now(),
    )
