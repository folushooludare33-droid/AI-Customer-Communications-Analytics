from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class RawEmail:
    customer_name: str
    customer_email: str
    subject: str
    body: str
    received_at: datetime
    product: str