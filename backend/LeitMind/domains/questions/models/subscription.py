from domains.base import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

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

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "sub_category_id": self.sub_category_id,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }