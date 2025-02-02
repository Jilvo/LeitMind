from domains.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class UserSubscription(Base):
    __tablename__ = "user_subscriptions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=True)
    sub_category_id = Column(Integer, ForeignKey("sub_categories.id", ondelete="CASCADE"), nullable=True)
    created_at = Column(DateTime, server_default=func.now())

    # Relations
    user = relationship("User", back_populates="subscriptions")
    category = relationship("Category", back_populates="subscriptions")
    sub_category = relationship("SubCategory", back_populates="subscriptions")
