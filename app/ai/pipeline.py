"""
AI enrichment pipeline.
"""

from app.ai.classifier import CategoryClassifier
from app.ai.department import DepartmentRouter
from app.ai.models import AIAnalysis
from app.ai.priority import PriorityClassifier
from app.ai.reply_generator import ReplyGenerator
from app.ai.sentiment import SentimentAnalyzer
from app.ai.summarizer import Summarizer


class AIPipeline:
    """Coordinates AI processing."""

    def __init__(self) -> None:
        self.classifier = CategoryClassifier()
        self.department = DepartmentRouter()
        self.priority = PriorityClassifier()
        self.sentiment = SentimentAnalyzer()
        self.summary = Summarizer()
        self.reply = ReplyGenerator()

    def analyze(
        self,
        customer_name: str,
        subject: str,
        body: str,
    ) -> AIAnalysis:
        """
        Analyze an email and return AI-generated metadata.
        """

        text = f"{subject}\n{body}"

        category = self.classifier.classify(text)
        department = self.department.route(category)
        priority = self.priority.classify(text)
        sentiment = self.sentiment.analyze(text)
        summary = self.summary.generate(subject, body)
        reply = self.reply.generate(customer_name)

        return AIAnalysis(
            category=category,
            department=department,
            priority=priority,
            sentiment=sentiment,
            summary=summary,
            draft_reply=reply,
        )