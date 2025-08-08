"""initial_migration

Revision ID: bfb1dd1c2af1
Revises: 
Create Date: 2025-08-08 16:16:40.053923

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bfb1dd1c2af1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Import des modèles pour créer les tables
    from domains.base import Base
    from domains import models_loader  # noqa: F401
    
    # Créer toutes les tables
    from sqlalchemy import create_engine
    from kink import di
    from controller import global_parameters  # noqa: F401
    
    database_url = di["POSTGRES_DB_URL"]
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)


def downgrade() -> None:
    # Import des modèles
    from domains.base import Base
    from domains import models_loader  # noqa: F401
    
    # Supprimer toutes les tables
    from sqlalchemy import create_engine
    from kink import di
    from controller import global_parameters  # noqa: F401
    
    database_url = di["POSTGRES_DB_URL"]
    engine = create_engine(database_url)
    Base.metadata.drop_all(engine)
