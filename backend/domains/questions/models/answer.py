from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from domains.base import Base


class Answer(Base):
    __tablename__ = "answers"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    question_id = Column(
        Integer,
        ForeignKey(
            "questions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    is_correct = Column(
        Boolean,
        nullable=False,
    )
    text = Column(
        String,
        nullable=False,
    )

    # Relation avec la question
    question = relationship(
        "Question",
        back_populates="answers",
        foreign_keys=[question_id],
    )

    def to_dict(
        self,
    ):
        return {
            "id": self.id,
            "question_id": self.question_id,
            "is_correct": self.is_correct,
            "text": self.text,
        }
