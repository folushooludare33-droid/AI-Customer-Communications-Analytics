from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class GeneratedEmail:
    customer_name: str
    customer_email: str
    subject: str
    body: str
    received_at: datetime

    product: str
    category: str
    department: str

    priority: str
    sentiment: str

    message_id: str
    summary: str
    draft_reply: str
    status: str