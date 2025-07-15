from domains.base import Base
from sqlalchemy import (TIMESTAMP, CheckConstraint, Column, ForeignKey,
                        Integer, String)
from sqlalchemy.sql import func


class SocialConnection(Base):
    __tablename__ = "social_connections"

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
    friend_id = Column(
        Integer,
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    status = Column(
        String(20),
        nullable=False,
    )
    connected_at = Column(
        TIMESTAMP,
        server_default=func.now(),
    )

    __table_args__ = (
        CheckConstraint(
            status.in_(
                [
                    "pending",
                    "accepted",
                    "blocked",
                ]
            ),
            name="check_status",
        ),
    )
