from domains.base import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class SubTheme(Base):
    __tablename__ = "sub_themes"

    id = Column(
        Integer,
        primary_key=True,
    )
    name = Column(
        String(100),
        unique=True,
        nullable=False,
    )
    description = Column(Text, nullable=True)
    
    created_at = Column(
        TIMESTAMP,
        server_default=func.now(),
    )
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now(),
    )
    
    questions = relationship("Question", back_populates="sub_theme")
