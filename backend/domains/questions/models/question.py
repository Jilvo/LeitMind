from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from domains.base import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    text = Column(
        Text,
        nullable=False,
    )
    category_id = Column(
        Integer,
        ForeignKey(
            "categories.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    theme_id = Column(Integer, ForeignKey("themes.id", ondelete="CASCADE"), nullable=True)
    sub_theme_id = Column(
        Integer,
        ForeignKey(
            "sub_themes.id",
            ondelete="CASCADE",
        ),
        nullable=True,
    )
    creator_id = Column(
        Integer,
        ForeignKey(
            "users.id",
            ondelete="SET NULL",
        ),
    )
    explanation = Column(Text)
    image_path = Column(
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

    # Relations avec les autres tables
    answers = relationship(
        "Answer",
        back_populates="question",
        cascade="all, delete-orphan",
        foreign_keys="[Answer.question_id]",
    )

    creator = relationship(
        "User",
        back_populates="questions",
    )
    category = relationship(
        "Category",
        back_populates="questions",
    )
    sub_theme = relationship(
        "SubTheme",
        back_populates="questions",
    )
    themes = relationship(
        "Theme",
        back_populates="questions",
    )

    def to_dict(
        self,
    ):
        return {
            "id": self.id,
            "text": self.text,
            "category_id": self.category_id,
            "creator_id": self.creator_id,
            "explanation": self.explanation,
            "image_path": self.image_path,
            "created_at": (self.created_at.isoformat() if self.created_at else None),
            "updated_at": (self.updated_at.isoformat() if self.updated_at else None),
        }
