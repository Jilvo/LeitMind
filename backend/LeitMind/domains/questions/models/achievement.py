from domains.base import (
    Base,
)
from sqlalchemy import (
    TIMESTAMP,
    Column,
    Integer,
    String,
    Text,
)
from sqlalchemy.sql import (
    func,
)


class Achievement(Base):
    __tablename__ = "achievements"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    name = Column(
        String(100),
        nullable=False,
    )
    description = Column(Text)
    icon_path = Column(Text)
    created_at = Column(
        TIMESTAMP,
        server_default=func.now(),
    )
