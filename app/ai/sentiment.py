"""
Rule-based sentiment analyzer.
"""


class SentimentAnalyzer:
    """
    Performs simple sentiment classification.
    """

    NEGATIVE_KEYWORDS = {
        "broken",
        "refund",
        "error",
        "damage",
        "replacement",
        "crash",
        "late",
    }

    def analyze(
        self,
        text: str,
    ) -> str:
        """
        Analyze the sentiment of text.
        """

        lowered = text.lower()

        if any(word in lowered for word in self.NEGATIVE_KEYWORDS):
            return "Negative"

        return "Neutral"