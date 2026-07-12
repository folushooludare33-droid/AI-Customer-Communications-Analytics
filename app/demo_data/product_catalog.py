"""
NovaTech product catalog.

This module contains every product that can appear in the synthetic
customer communication dataset.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    """Represents a product sold by NovaTech."""

    name: str
    category: str


PRODUCTS: list[Product] = [
    Product("NovaBook Air 13", "Laptop"),
    Product("NovaBook Pro 15", "Laptop"),
    Product("NovaPhone X", "Smartphone"),
    Product("NovaPhone Lite", "Smartphone"),
    Product("NovaTab 11", "Tablet"),
    Product("NovaTab Mini", "Tablet"),
    Product("NovaWatch Active", "Smart Watch"),
    Product("NovaWatch Pro", "Smart Watch"),
    Product("NovaBuds Pro", "Wireless Earbuds"),
    Product("NovaBuds Lite", "Wireless Earbuds"),
    Product("65W Fast Charger", "Charger"),
    Product("Wireless Charging Pad", "Accessory"),
    Product("USB-C Cable", "Accessory"),
    Product("Laptop Sleeve", "Accessory"),
]