"""
Input Validation Functions
"""

from bot.exceptions import ValidationError
from bot.constants import (
    SUPPORTED_ORDER_TYPES,
    SUPPORTED_SIDES
)


def validate_symbol(symbol):
    """
    Validate trading symbol.
    Example: BTCUSDT
    """
    if not symbol:
        raise ValidationError("Symbol cannot be empty.")

    symbol = symbol.upper().strip()

    if len(symbol) < 6:
        raise ValidationError("Invalid trading symbol.")

    return symbol


def validate_side(side):
    """
    Validate BUY / SELL
    """
    side = side.upper().strip()

    if side not in SUPPORTED_SIDES:
        raise ValidationError(
            f"Side must be one of {SUPPORTED_SIDES}"
        )

    return side


def validate_order_type(order_type):
    """
    Validate MARKET / LIMIT
    """
    order_type = order_type.upper().strip()

    if order_type not in SUPPORTED_ORDER_TYPES:
        raise ValidationError(
            f"Order type must be one of {SUPPORTED_ORDER_TYPES}"
        )

    return order_type


def validate_quantity(quantity):
    """
    Validate quantity.
    """
    try:
        quantity = float(quantity)
    except ValueError:
        raise ValidationError(
            "Quantity must be numeric."
        )

    if quantity <= 0:
        raise ValidationError(
            "Quantity must be greater than zero."
        )

    return quantity


def validate_price(price):
    """
    Validate price.
    """
    try:
        price = float(price)
    except ValueError:
        raise ValidationError(
            "Price must be numeric."
        )

    if price <= 0:
        raise ValidationError(
            "Price must be greater than zero."
        )

    return price