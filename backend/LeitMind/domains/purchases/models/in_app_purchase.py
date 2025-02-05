from domains.base import (
    Base,
)
from sqlalchemy import (
    DECIMAL,
    TIMESTAMP,
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.sql import (
    func,
)


class InAppPurchase(Base):
    __tablename__ = "in_app_purchases"

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
    item_name = Column(
        String(100),
        nullable=False,
    )
    price = Column(
        DECIMAL(
            10,
            2,
        ),
        nullable=False,
    )
    currency = Column(
        String(10),
        nullable=False,
    )
    purchased_at = Column(
        TIMESTAMP,
        server_default=func.now(),
    )
