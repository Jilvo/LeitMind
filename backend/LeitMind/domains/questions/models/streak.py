from sqlalchemy import Column, Date, ForeignKey, Integer

from domains.base import Base


class Streak(Base):
    __tablename__ = "streaks"

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
    current_streak = Column(
        Integer,
        default=0,
    )
    best_streak = Column(
        Integer,
        default=0,
    )
    last_active_date = Column(Date)
