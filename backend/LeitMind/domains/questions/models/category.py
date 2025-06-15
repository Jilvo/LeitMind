from sqlalchemy import TIMESTAMP, Column, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from domains.base import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    name = Column(
        String(50),
        unique=True,
        nullable=False,
    )
    description = Column(
        Text,
        nullable=True,
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

    sub_categories = relationship(
        "SubCategory",
        back_populates="category",
    )
    questions = relationship(
        "Question",
        back_populates="category",
        cascade="all, delete-orphan",
    )

    def to_dict(
        self,
    ):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": (self.created_at.isoformat() if self.created_at else None),
            "updated_at": (self.updated_at.isoformat() if self.updated_at else None),
        }
