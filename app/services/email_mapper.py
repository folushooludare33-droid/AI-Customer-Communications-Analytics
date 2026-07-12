"""
Maps generated email objects to SQLAlchemy ORM models.
"""

from app.demo_data.generator_models import GeneratedEmail
from app.models.customer_email import CustomerEmail


def to_customer_email(email: GeneratedEmail) -> CustomerEmail:
    """
    Convert a GeneratedEmail into a CustomerEmail ORM object.
    """

    return CustomerEmail(
        message_id=email.message_id,
        customer_name=email.customer_name,
        customer_email=email.customer_email,
        subject=email.subject,
        body=email.body,
        received_at=email.received_at,
        product=email.product,
        category=email.category,
        department=email.department,
        priority=email.priority,
        sentiment=email.sentiment,
        summary=email.summary,
        draft_reply=email.draft_reply,
        status=email.status,
    )