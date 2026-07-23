"""
Application Constants
"""

APP_NAME = "Binance Futures Trading Bot"
APP_VERSION = "1.0.0"

# Binance Futures Testnet
BASE_URL = "https://testnet.binancefuture.com"

# Supported Order Types
MARKET_ORDER = "MARKET"
LIMIT_ORDER = "LIMIT"

# Supported Sides
BUY = "BUY"
SELL = "SELL"

SUPPORTED_ORDER_TYPES = [
    MARKET_ORDER,
    LIMIT_ORDER
]

SUPPORTED_SIDES = [
    BUY,
    SELL
]

# Logging
LOG_FILE = "logs/trading_bot.log"
LOG_LEVEL = "INFO"

# Retry Settings
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 2