from domains.base import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer
from sqlalchemy.sql import func


class Attempt(Base):
    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False)
    is_correct = Column(Boolean, nullable=False)
    attempted_at = Column(TIMESTAMP, server_default=func.now())
