"""
Analytics for customer email data.
"""

from collections import Counter

from app.models.customer_email import CustomerEmail


class EmailAnalytics:
    """Generates business metrics from customer emails."""

    @staticmethod
    def count_by_category(emails: list[CustomerEmail]) -> dict[str, int]:
        return dict(Counter(email.category for email in emails))

    @staticmethod
    def count_by_department(emails: list[CustomerEmail]) -> dict[str, int]:
        return dict(Counter(email.department for email in emails))

    @staticmethod
    def count_by_priority(emails: list[CustomerEmail]) -> dict[str, int]:
        return dict(Counter(email.priority for email in emails))

    @staticmethod
    def count_by_sentiment(emails: list[CustomerEmail]) -> dict[str, int]:
        return dict(Counter(email.sentiment for email in emails))

    @staticmethod
    def total_emails(emails: list[CustomerEmail]) -> int:
        return len(emails)

    @staticmethod
    def open_emails(emails: list[CustomerEmail]) -> int:
        return sum(email.status == "Open" for email in emails)

    @staticmethod
    def closed_emails(emails: list[CustomerEmail]) -> int:
        return sum(email.status == "Closed" for email in emails)