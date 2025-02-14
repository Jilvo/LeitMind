from kink import di
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configure l'engine
engine = create_engine(
    di["POSTGRES_DB_URL"],
    echo=True,
)

# Configure le sessionmaker
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
