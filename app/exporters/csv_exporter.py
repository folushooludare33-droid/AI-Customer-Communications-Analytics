"""
Exports customer communication data to CSV.
"""

from pathlib import Path

import csv

from sqlalchemy.orm import Session

from app.config.settings import settings
from app.models.customer_email import CustomerEmail


class CSVExporter:
    """
    Exports customer email records to CSV.
    """

    def export(
        self,
        session: Session,
        filename: str = "customer_emails.csv",
    ) -> Path:
        records = (
            session.query(CustomerEmail)
            .order_by(CustomerEmail.received_at)
            .all()
        )

        output_path = (
            settings.exports_dir /
            filename
        )

        with output_path.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow([
                "message_id",
                "customer_name",
                "customer_email",
                "subject",
                "body",
                "received_at",
                "product",
                "category",
                "department",
                "priority",
                "sentiment",
                "summary",
                "draft_reply",
                "status",
            ])

            for row in records:
                writer.writerow([
                    row.message_id,
                    row.customer_name,
                    row.customer_email,
                    row.subject,
                    row.body,
                    row.received_at,
                    row.product,
                    row.category,
                    row.department,
                    row.priority,
                    row.sentiment,
                    row.summary,
                    row.draft_reply,
                    row.status,
                ])

        return output_path