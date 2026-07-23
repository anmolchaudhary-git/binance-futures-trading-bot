"""
Custom Exceptions for Trading Bot
"""


class TradingBotError(Exception):
    """Base exception for all trading bot errors."""
    pass


class ConfigurationError(TradingBotError):
    """Raised when configuration is invalid."""
    pass


class ValidationError(TradingBotError):
    """Raised when user input validation fails."""
    pass


class APIConnectionError(TradingBotError):
    """Raised when API connection fails."""
    pass


class OrderError(TradingBotError):
    """Raised when order placement fails."""
    pass


class AuthenticationError(TradingBotError):
    """Raised when API credentials are invalid."""
    pass


class InsufficientBalanceError(TradingBotError):
    """Raised when account balance is insufficient."""
    pass


class SymbolNotFoundError(TradingBotError):
    """Raised when trading symbol is invalid."""
    pass