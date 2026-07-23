"""
Logging Configuration
"""

import logging
import os

# Create logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

LOG_FILE = "logs/trading_bot.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("TradingBot")


def log_info(message):
    """Log information message."""
    logger.info(message)


def log_warning(message):
    """Log warning message."""
    logger.warning(message)


def log_error(message):
    """Log error message."""
    logger.error(message)


def log_debug(message):
    """Log debug message."""
    logger.debug(message)