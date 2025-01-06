from domains.base import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class SubCategory(Base):
    __tablename__ = "sub_categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    country = Column(
        String(2),
        nullable=False,
        default="GL",
    )
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    category = relationship("Category", back_populates="sub_categories")
    themes = relationship("Theme", back_populates="sub_category")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category_id": self.category_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
