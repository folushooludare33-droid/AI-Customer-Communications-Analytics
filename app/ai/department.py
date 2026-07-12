"""
Department routing.
"""


class DepartmentRouter:
    """Routes emails to departments."""

    MAPPING = {
        "Delivery": "Logistics",
        "Billing": "Finance",
        "Technical Support": "Technical Support",
        "Returns": "Returns",
        "Warranty": "Warranty",
    }

    def route(self, category: str) -> str:
        return self.MAPPING.get(category, "Customer Support")