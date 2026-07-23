"""
Order Management Module
"""

from binance.enums import (
    SIDE_BUY,
    SIDE_SELL,
    ORDER_TYPE_MARKET,
    ORDER_TYPE_LIMIT,
    TIME_IN_FORCE_GTC
)

from bot.validators import (
    validate_symbol,
    validate_side,
    validate_quantity,
    validate_price
)

from bot.logging_config import logger


class OrderManager:

    def __init__(self, client):
        """
        Initialize Order Manager
        """

        self.client = client


    def market_order(
        self,
        symbol,
        side,
        quantity
    ):
        """
        Place Market Order
        """

        symbol = validate_symbol(symbol)
        side = validate_side(side)
        quantity = validate_quantity(quantity)

        order_side = (
            SIDE_BUY
            if side == "BUY"
            else SIDE_SELL
        )

        response = self.client.create_order(
            symbol=symbol,
            side=order_side,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )

        logger.info(
            "Market order placed successfully"
        )

        return response


    def limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):
        """
        Place Limit Order
        """

        symbol = validate_symbol(symbol)
        side = validate_side(side)
        quantity = validate_quantity(quantity)
        price = validate_price(price)

        order_side = (
            SIDE_BUY
            if side == "BUY"
            else SIDE_SELL
        )

        response = self.client.create_order(
            symbol=symbol,
            side=order_side,
            type=ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC
        )

        logger.info(
            "Limit order placed successfully"
        )

        return response


    def cancel(
        self,
        symbol,
        order_id
    ):
        """
        Cancel Order
        """

        return self.client.cancel_order(
            symbol,
            order_id
        )


    def status(
        self,
        symbol,
        order_id
    ):
        """
        Check Order Status
        """

        return self.client.get_order_status(
            symbol,
            order_id
        )


    def open_orders(
        self,
        symbol
    ):
        """
        Get Open Orders
        """

        return self.client.get_open_orders(
            symbol
        )