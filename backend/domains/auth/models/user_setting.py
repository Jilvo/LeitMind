from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.sql import func

from domains.base import Base


class UserSetting(Base):
    __tablename__ = "user_settings"

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
    language = Column(
        String(10),
        default="en",
    )
    notification_frequency = Column(
        String(20),
        default="daily",
    )
    theme = Column(
        String(10),
        default="light",
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
