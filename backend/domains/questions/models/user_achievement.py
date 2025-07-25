from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer
from sqlalchemy.sql import func

from domains.base import Base


class UserAchievement(Base):
    __tablename__ = "user_achievements"

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
    achievement_id = Column(
        Integer,
        ForeignKey(
            "achievements.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    unlocked_at = Column(
        TIMESTAMP,
        server_default=func.now(),
    )
