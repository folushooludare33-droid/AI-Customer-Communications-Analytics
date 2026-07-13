"""
Rule-based priority classifier.
"""


class PriorityClassifier:
    """Determines email priority."""

    HIGH = ("broken", "refund", "replacement", "damage", "crash")
    MEDIUM = ("battery", "delivery", "tracking", "warranty")

    def classify(self, text: str) -> str:
        text = text.lower()

        if any(word in text for word in self.HIGH):
            return "High"

        if any(word in text for word in self.MEDIUM):
            return "Medium"

        return "Low"