from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, Text
from sqlalchemy.sql import func

from domains.base import Base


class Notification(Base):
    __tablename__ = "notifications"

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
    message = Column(
        Text,
        nullable=False,
    )
    is_read = Column(
        Boolean,
        default=False,
    )
    sent_at = Column(
        TIMESTAMP,
        server_default=func.now(),
    )
