"""
Synthetic customer personas.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CustomerPersona:
    first_name: str
    last_name: str
    email_domain: str


CUSTOMERS: list[CustomerPersona] = [
    CustomerPersona("James", "Wilson", "gmail.com"),
    CustomerPersona("Sophia", "Johnson", "outlook.com"),
    CustomerPersona("Michael", "Brown", "yahoo.com"),
    CustomerPersona("Emily", "Davis", "gmail.com"),
    CustomerPersona("Daniel", "Martinez", "hotmail.com"),
    CustomerPersona("Olivia", "Taylor", "icloud.com"),
    CustomerPersona("Ethan", "Anderson", "gmail.com"),
    CustomerPersona("Ava", "Thomas", "outlook.com"),
    CustomerPersona("Benjamin", "Jackson", "gmail.com"),
    CustomerPersona("Charlotte", "White", "yahoo.com"),
]