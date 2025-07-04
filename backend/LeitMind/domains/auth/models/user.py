from sqlalchemy import (TIMESTAMP, Column, DateTime, ForeignKey, Integer,
                        String, Text, func)
from sqlalchemy.orm import relationship

from domains.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    username = Column(
        String(50),
        unique=True,
        nullable=False,
    )
    email = Column(
        String(100),
        unique=True,
        nullable=False,
    )
    hashed_password = Column(
        Text,
        nullable=False,
    )
    country = Column(
        String(50),
        nullable=False,
    )
    created_at = Column(
        DateTime,
        server_default=func.now(),
    )
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
    )

    questions = relationship(
        "Question",
        back_populates="creator",
    )

    subscriptions = relationship(
        "UserSubscription",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    def to_dict(
        self,
    ):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "country": self.country,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
        }
