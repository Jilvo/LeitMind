from domains.base import (
    Base,
)
from sqlalchemy import (
    TIMESTAMP,
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import (
    relationship,
)
from sqlalchemy.sql import (
    func,
)


class Theme(Base):
    __tablename__ = "themes"

    id = Column(
        Integer,
        primary_key=True,
    )
    name = Column(
        String(100),
        unique=True,
        nullable=False,
    )
    description = Column(Text)
    sub_category_id = Column(
        Integer,
        ForeignKey(
            "sub_categories.id",
            ondelete="CASCADE",
        ),
        nullable=False,
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

    sub_category = relationship(
        "SubCategory",
        back_populates="themes",
    )

    def to_dict(
        self,
    ):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "sub_category_id": self.sub_category_id,
            "created_at": (self.created_at.isoformat() if self.created_at else None),
            "updated_at": (self.updated_at.isoformat() if self.updated_at else None),
        }
