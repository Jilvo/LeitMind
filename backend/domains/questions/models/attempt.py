from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from domains.base import Base


class Attempt(Base):
    __tablename__ = "attempts"

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
    answer_id = Column(
        Integer,
        ForeignKey(
            "answers.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    attempted_at = Column(
        TIMESTAMP,
        server_default=func.now(),
    )
    attempt_count = Column(
        Integer,
        nullable=False,
        default=1,
    )
    leitner_box = Column(
        Integer,
        default=1,
    )  # 1 : 1 day, 2 : 3 days, 3 : 7 days, 4 : 15 days, 5 : 30 days

    user = relationship("User", back_populates="attempts")
    question = relationship("Question", back_populates="attempts")
    answer = relationship("Answer", back_populates="attempts")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "question": self.question.text if self.question else None,
            "is_correct": self.is_correct,
            "answer": self.answer.text if self.answer else None,
            "attempted_at": self.attempted_at.isoformat() if self.attempted_at else None,
            "attempt_count": self.attempt_count,
            "leitner_box": self.leitner_box,
        }