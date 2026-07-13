"""
Category classifier.
"""


class CategoryClassifier:
    """Simple rule-based classifier."""

    KEYWORDS = {
        "Delivery": ["delivery", "tracking", "shipment"],
        "Billing": ["refund", "payment", "charged"],
        "Technical Support": ["battery", "broken", "error", "crash"],
        "Returns": ["return", "replacement"],
        "Warranty": ["warranty", "repair"],
    }

    def classify(self, text: str) -> str:
        text = text.lower()

        for category, words in self.KEYWORDS.items():
            if any(word in text for word in words):
                return category

        return "General Inquiry"