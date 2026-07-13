"""
Synthetic customer email generator.
"""

from __future__ import annotations

import random
import uuid
from datetime import datetime, timedelta

from app.demo_data.customer_personas import CUSTOMERS
from app.demo_data.email_templates import CLOSINGS, OPENINGS
from app.demo_data.generator_models import GeneratedEmail
from app.demo_data.issue_taxonomy import ISSUES
from app.demo_data.product_catalog import PRODUCTS


class SyntheticEmailGenerator:
    """Generates realistic customer emails."""

    DEPARTMENT_MAP = {
        "Delivery": "Logistics",
        "Billing": "Finance",
        "Technical Support": "Technical Support",
        "Returns": "Returns",
        "Warranty": "Warranty",
    }

    PRIORITIES = [
        "Low",
        "Medium",
        "High",
    ]

    SENTIMENTS = [
        "Positive",
        "Neutral",
        "Negative",
    ]

    def __init__(self) -> None:
        self.random = random.Random()

    def generate_timestamp(self) -> datetime:
        """
        Generate a realistic timestamp within the last 180 days.
        """
        days = self.random.randint(0, 180)
        hours = self.random.randint(0, 23)
        minutes = self.random.randint(0, 59)

        return datetime.now() - timedelta(
            days=days,
            hours=hours,
            minutes=minutes,
        )

    def generate_message_id(self) -> str:
        """
        Generate a unique message identifier.
        """
        return str(uuid.uuid4())

    def generate_summary(
        self,
        product: str,
        issue: str,
    ) -> str:
        """
        Create a concise summary of the email.
        """
        return (
            f"Customer reports '{issue}' "
            f"for {product}."
        )

    def generate_draft_reply(
        self,
        customer_name: str,
    ) -> str:
        """
        Create a professional draft reply.
        """
        return (
            f"Dear {customer_name},\n\n"
            "Thank you for contacting NovaTech Support. "
            "We have received your request and our team "
            "is reviewing the issue. "
            "We will get back to you shortly.\n\n"
            "Kind regards,\n"
            "NovaTech Customer Support"
        )

    def get_customer(self):
        """
        Select a random customer persona.
        """
        customer = self.random.choice(CUSTOMERS)

        full_name = f"{customer.first_name} {customer.last_name}"

        email = (
            f"{customer.first_name.lower()}."
            f"{customer.last_name.lower()}"
            f"{self.random.randint(10, 999)}"
            f"@{customer.email_domain}"
        )

        return customer, full_name, email

    def get_product(self):
        """
        Select a random product.
        """
        return self.random.choice(PRODUCTS)

    def get_issue(self):
        """
        Select a business category and issue.
        """
        category = self.random.choice(list(ISSUES.keys()))
        issue = self.random.choice(ISSUES[category])

        return category, issue

    def build_subject(
        self,
        product_name: str,
        issue: str,
    ) -> str:
        """
        Generate a realistic email subject.
        """
        templates = [
            f"{product_name} - {issue}",
            f"Need help with my {product_name}",
            f"Problem with {product_name}",
            f"Assistance required for {product_name}",
            f"{issue} on my {product_name}",
        ]

        return self.random.choice(templates)

    def build_body(
        self,
        product_name: str,
        issue: str,
    ) -> str:
        """
        Construct a realistic customer email.
        """
        opening = self.random.choice(OPENINGS)
        closing = self.random.choice(CLOSINGS)

        return (
            f"{opening}\n\n"
            f"I recently purchased the {product_name} and "
            f"I've been experiencing the following issue: "
            f"{issue}.\n\n"
            f"I would appreciate your assistance in resolving "
            f"this problem as soon as possible.\n\n"
            f"{closing}"
        )

    def get_department(
        self,
        category: str,
    ) -> str:
        """
        Determine which department should handle the issue.
        """
        return self.DEPARTMENT_MAP[category]

    def get_priority(self) -> str:
        """
        Select a priority level.
        """
        weights = [0.25, 0.50, 0.25]

        return self.random.choices(
            self.PRIORITIES,
            weights=weights,
            k=1,
        )[0]

    def get_sentiment(self) -> str:
        """
        Select a customer sentiment.
        """
        weights = [0.20, 0.30, 0.50]

        return self.random.choices(
            self.SENTIMENTS,
            weights=weights,
            k=1,
        )[0]

    def generate_email(self) -> GeneratedEmail:
        """
        Generate one synthetic customer email.
        """
        _, customer_name, customer_email = self.get_customer()

        product = self.get_product()
        category, issue = self.get_issue()

        subject = self.build_subject(
            product.name,
            issue,
        )

        body = self.build_body(
            product.name,
            issue,
        )

        return GeneratedEmail(
            customer_name=customer_name,
            customer_email=customer_email,
            subject=subject,
            body=body,
            received_at=self.generate_timestamp(),

            product=product.name,
            category=category,
            department=self.get_department(category),

            priority=self.get_priority(),
            sentiment=self.get_sentiment(),

            message_id=self.generate_message_id(),
            summary=self.generate_summary(
                product.name,
                issue,
            ),
            draft_reply=self.generate_draft_reply(
                customer_name,
            ),
            status="Open",
        )