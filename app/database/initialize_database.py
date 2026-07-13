from app.database.base import Base
from app.database.session import engine

# Import models so SQLAlchemy registers them
from app.models.customer_email import CustomerEmail  # noqa: F401


def initialize_database() -> None:
    """Create all database tables if they do not exist."""
    Base.metadata.create_all(bind=engine)