from domains.base import Base
from infrastructure.spi.repository.database import engine


# Crée toutes les tables
def init_db():
    Base.metadata.create_all(bind=engine)
