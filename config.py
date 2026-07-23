"""
Configuration Module
Loads environment variables for Binance Futures Testnet.
"""

import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# API Credentials
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

# Binance Futures Testnet URL
BASE_URL = os.getenv(
    "BASE_URL",
    "https://testnet.binancefuture.com"
)

# Application Settings
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

# Validate API Keys
if not BINANCE_API_KEY:
    raise ValueError(
        "BINANCE_API_KEY not found in .env file."
    )

if not BINANCE_API_SECRET:
    raise ValueError(
        "BINANCE_API_SECRET not found in .env file."
    )