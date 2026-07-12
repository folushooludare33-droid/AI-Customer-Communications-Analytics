"""
Rule-based draft reply generator.
"""


class ReplyGenerator:
    """
    Generates professional draft replies.
    """

    def generate(
        self,
        customer_name: str,
    ) -> str:
        return (
            f"Dear {customer_name},\n\n"
            "Thank you for contacting NovaTech Support. "
            "Your request has been received and assigned "
            "to the appropriate team.\n\n"
            "Kind regards,\n"
            "NovaTech Support"
        )