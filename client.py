"""
Binance Futures Client
"""

from binance.client import Client
from binance.exceptions import BinanceAPIException

from bot.config import (
    BINANCE_API_KEY,
    BINANCE_API_SECRET,
    BASE_URL
)

from bot.logging_config import logger


class BinanceClient:

    def __init__(self):
        """
        Initialize Binance Client
        """

        self.client = Client(
            BINANCE_API_KEY,
            BINANCE_API_SECRET
        )

        # Use Binance Futures Testnet
        self.client.FUTURES_URL = BASE_URL

        logger.info(
            "Connected to Binance Futures Testnet"
        )

    def ping(self):
        """
        Check API connection
        """

        try:

            self.client.futures_ping()

            return True

        except BinanceAPIException as e:

            logger.error(e)

            return False

    def get_server_time(self):
        """
        Get Binance Server Time
        """

        return self.client.futures_time()
          def get_account_balance(self):
        """
        Get Futures account balance
        """

        try:

            return self.client.futures_account_balance()

        except BinanceAPIException as e:

            logger.error(e)

            raise e


    def get_account_info(self):
        """
        Get complete account information
        """

        try:

            return self.client.futures_account()

        except BinanceAPIException as e:

            logger.error(e)

            raise e


    def get_positions(self):
        """
        Get current positions
        """

        try:

            return self.client.futures_position_information()

        except BinanceAPIException as e:

            logger.error(e)

            raise e


    def get_open_orders(self, symbol):
        """
        Get open orders for symbol
        """

        try:

            return self.client.futures_get_open_orders(
                symbol=symbol.upper()
            )

        except BinanceAPIException as e:

            logger.error(e)

            raise e    def create_order(self, **order_data):
        """
        Create Futures Order
        """

        try:

            response = self.client.futures_create_order(
                **order_data
            )

            logger.info(
                f"Order created: {response.get('orderId')}"
            )

            return response

        except BinanceAPIException as e:

            logger.error(e)

            raise e


    def get_order_status(self, symbol, order_id):
        """
        Get order status
        """

        try:

            return self.client.futures_get_order(
                symbol=symbol.upper(),
                orderId=order_id
            )

        except BinanceAPIException as e:

            logger.error(e)

            raise e


    def cancel_order(self, symbol, order_id):
        """
        Cancel existing order
        """

        try:

            response = self.client.futures_cancel_order(
                symbol=symbol.upper(),
                orderId=order_id
            )

            logger.info(
                f"Order cancelled: {order_id}"
            )

            return response

        except BinanceAPIException as e:

            logger.error(e)

            raise e
              def create_order(self, **order_data):
        """
        Create Futures Order
        """

        try:

            response = self.client.futures_create_order(
                **order_data
            )

            logger.info(
                f"Order created: {response.get('orderId')}"
            )

            return response

        except BinanceAPIException as e:

            logger.error(e)

            raise e


    def get_order_status(self, symbol, order_id):
        """
        Get order status
        """

        try:

            return self.client.futures_get_order(
                symbol=symbol.upper(),
                orderId=order_id
            )

        except BinanceAPIException as e:

            logger.error(e)

            raise e
              def create_order(self, **order_data):
        """
        Create Futures Order
        """

        try:

            response = self.client.futures_create_order(
                **order_data
            )

            logger.info(
                f"Order created: {response.get('orderId')}"
            )

            return response

        except BinanceAPIException as e:

            logger.error(e)

            raise e


    def get_order_status(self, symbol, order_id):
        """
        Get order status
        """

        try:

            return self.client.futures_get_order(
                symbol=symbol.upper(),
                orderId=order_id
            )

        except BinanceAPIException as e:

            logger.error(e)

            raise e


    def cancel_order(self, symbol, order_id):
        """
        Cancel existing order
        """

        try:

            response = self.client.futures_cancel_order(
                symbol=symbol.upper(),
                orderId=order_id
            )

            logger.info(
                f"Order cancelled: {order_id}"
            )

            return response

        except BinanceAPIException as e:

            logger.error(e)

            raise e