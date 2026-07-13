"""
Business issue taxonomy for customer communications.
"""

ISSUES: dict[str, list[str]] = {
    "Delivery": [
        "Delayed shipment",
        "Package never arrived",
        "Tracking not updating",
    ],
    "Billing": [
        "Incorrect charge",
        "Refund request",
        "Duplicate payment",
    ],
    "Technical Support": [
        "Device won't power on",
        "Battery drains quickly",
        "Software crashes",
    ],
    "Returns": [
        "Requesting replacement",
        "Requesting return",
        "Wrong item received",
    ],
    "Warranty": [
        "Warranty claim",
        "Repair status",
        "Coverage question",
    ],
}