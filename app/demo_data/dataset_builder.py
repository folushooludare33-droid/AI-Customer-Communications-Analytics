"""
Builds synthetic customer communication datasets.
"""

from app.ai.pipeline import AIPipeline
from app.demo_data.generator_models import GeneratedEmail
from app.demo_data.synthetic_generator import SyntheticEmailGenerator


class DatasetBuilder:
    """
    Creates collections of synthetic customer emails.
    """

    def __init__(self) -> None:
        self.generator = SyntheticEmailGenerator()
        self.ai_pipeline = AIPipeline()

    def build_dataset(
        self,
        size: int,
    ) -> list[GeneratedEmail]:
        """
        Generate a dataset containing the requested
        number of synthetic emails.
        """
        emails: list[GeneratedEmail] = []

        for _ in range(size):
            email = self.generator.generate_email()

            analysis = self.ai_pipeline.analyze(
                customer_name=email.customer_name,
                subject=email.subject,
                body=email.body,
            )

            email.category = analysis.category
            email.department = analysis.department
            email.priority = analysis.priority
            email.sentiment = analysis.sentiment
            email.summary = analysis.summary
            email.draft_reply = analysis.draft_reply

            emails.append(email)

        return emails