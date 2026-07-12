"""
Imports generated emails into the database.
"""

from app.database.session import SessionLocal
from app.demo_data.generator_models import GeneratedEmail
from app.models.customer_email import CustomerEmail


class EmailImportService:
    """
    Imports synthetic emails into SQLite.
    """

    def __init__(self) -> None:
        self.session = SessionLocal()

    def import_emails(
        self,
        emails: list[GeneratedEmail],
    ) -> None:
        """
        Import generated emails into the database.
        """

        for email in emails:

            record = CustomerEmail(
                message_id=email.message_id,
                customer_name=email.customer_name,
                customer_email=email.customer_email,
                subject=email.subject,
                body=email.body,
                received_at=email.received_at,
                category=email.category,
                department=email.department,
                priority=email.priority,
                sentiment=email.sentiment,
                summary=email.summary,
                draft_reply=email.draft_reply,
                status=email.status,
            )

            self.session.add(record)

        self.session.commit()

    def close(self) -> None:
        """
        Close the database session.
        """

        self.session.close()

        """
Database import service.
"""

from sqlalchemy.orm import Session

from app.demo_data.generator_models import GeneratedEmail
from app.services.email_mapper import to_customer_email


class EmailImportService:
    """
    Imports generated emails into the database.
    """

    def import_emails(
        self,
        session: Session,
        emails: list[GeneratedEmail],
    ) -> None:
        """
        Import a collection of generated emails.
        """

        records = [
            to_customer_email(email)
            for email in emails
        ]

        session.add_all(records)

        session.commit()