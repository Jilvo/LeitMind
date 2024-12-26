from domains.base import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer
from sqlalchemy.sql import func


class VirtualCurrency(Base):
    __tablename__ = "virtual_currency"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    balance = Column(Integer, default=0)
    last_updated = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
