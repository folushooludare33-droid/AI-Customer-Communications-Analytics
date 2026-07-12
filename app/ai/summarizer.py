"""
Rule-based email summarizer.

Future versions can replace this implementation
with an OpenAI-powered summarizer without changing
the public interface.
"""


class Summarizer:
    """
    Generates a concise summary for an email.
    """

    def generate(
        self,
        subject: str,
        body: str,
    ) -> str:
        """
        Generate a summary.

        Currently rule-based.
        """

        return f"{subject}: {body[:80]}..."