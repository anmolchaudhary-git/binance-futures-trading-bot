"""
Utility Functions
"""

from datetime import datetime
import time


def get_current_time():
    """
    Returns current date and time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def retry_delay(seconds=2):
    """
    Wait before retrying an API request.
    """
    time.sleep(seconds)


def format_price(price):
    """
    Format price to 2 decimal places.
    """
    return round(float(price), 2)


def format_quantity(quantity):
    """
    Format quantity to 3 decimal places.
    """
    return round(float(quantity), 3)


def print_banner():
    """
    Display application banner.
    """
    print("=" * 50)
    print(" Binance Futures Testnet Trading Bot ")
    print("=" * 50)


def success(message):
    """
    Print success message.
    """
    print(f"[SUCCESS] {message}")


def error(message):
    """
    Print error message.
    """
    print(f"[ERROR] {message}")


def info(message):
    """
    Print information message.
    """
    print(f"[INFO] {message}")