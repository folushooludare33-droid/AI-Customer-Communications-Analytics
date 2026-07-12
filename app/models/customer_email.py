from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class CustomerEmail(Base):
    """Represents a customer email and its AI-generated analysis."""

    __tablename__ = "customer_emails"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    message_id: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    customer_name: Mapped[str] = mapped_column(String(100), nullable=False)

    customer_email: Mapped[str] = mapped_column(String(255), nullable=False)

    subject: Mapped[str] = mapped_column(String(255), nullable=False)

    body: Mapped[str] = mapped_column(Text, nullable=False)

    received_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    product: Mapped[str] = mapped_column(String(100), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)

    department: Mapped[str] = mapped_column(String(50), nullable=False)

    priority: Mapped[str] = mapped_column(String(20), nullable=False)

    sentiment: Mapped[str] = mapped_column(String(20), nullable=False)

    summary: Mapped[str] = mapped_column(Text, nullable=False)

    draft_reply: Mapped[str] = mapped_column(Text, nullable=False)

    status: Mapped[str] = mapped_column(String(20), default="new", nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )