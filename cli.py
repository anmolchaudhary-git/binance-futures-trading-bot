"""
Command Line Interface
Binance Futures Trading Bot
"""

import argparse

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.utils import print_banner


def main():

    print_banner()

    client = BinanceClient()

    order_manager = OrderManager(
        client
    )

    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    sub = parser.add_subparsers(
        dest="command"
    )


    # Market Order
    market = sub.add_parser(
        "market"
    )

    market.add_argument(
        "--symbol",
        required=True
    )

    market.add_argument(
        "--side",
        required=True
    )

    market.add_argument(
        "--quantity",
        required=True
    )


    # Limit Order
    limit = sub.add_parser(
        "limit"
    )

    limit.add_argument(
        "--symbol",
        required=True
    )

    limit.add_argument(
        "--side",
        required=True
    )

    limit.add_argument(
        "--quantity",
        required=True
    )

    limit.add_argument(
        "--price",
        required=True
    )


    # Balance
    sub.add_parser(
        "balance"
    )


    args = parser.parse_args()


    if args.command == "market":

        result = order_manager.market_order(
            args.symbol,
            args.side,
            args.quantity
        )

        print(result)


    elif args.command == "limit":

        result = order_manager.limit_order(
            args.symbol,
            args.side,
            args.quantity,
            args.price
        )

        print(result)


    elif args.command == "balance":

        result = client.get_account_balance()

        print(result)


    else:

        parser.print_help()



if __name__ == "__main__":
    main()