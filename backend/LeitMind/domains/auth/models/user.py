from domains.base import Base
from sqlalchemy import (TIMESTAMP, Column, DateTime, ForeignKey, Integer, String, Text,
                        func)
from sqlalchemy.orm import relationship


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
    
class UserSubscription(Base):
    __tablename__ = "user_subscriptions"

    id = Column(
        Integer,
        primary_key=True,
    )
    user_id = Column(
        Integer,
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    sub_category_id = Column(
        Integer,
        ForeignKey(
            "sub_categories.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    is_active = Column(
        Integer,
        nullable=False,
        default=1,
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
    # Relations avec les autres tables
    user = relationship(
        "User",
        back_populates="subscriptions",
        foreign_keys=[user_id],
    )
    sub_category = relationship(
        "SubCategory",
        back_populates="subscriptions",
        foreign_keys=[sub_category_id],
    )
