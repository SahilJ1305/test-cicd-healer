# src/formatter.py
# String formatting utilities for reports and display output

from datetime import datetime

def format_greeting(name: str) -> str:
    """Format a greeting message."""
    return f"Hello, {name}!"

def format_price(amount: float, currency: str = "USD") -> str:
    """Format a price with currency symbol."""
    symbols = {"USD": "$", "EUR": "€", "GBP": "£"}
    return f"{symbols.get(currency, '$')}{amount:,.2f}"

def repeat_word(word: str, count: int = 2) -> str:
    """Repeat a word multiple times."""
    return " ".join([word] * count)

def format_currency(amount: float, symbol: str = "$") -> str:
    """Format a float as a currency string."""
    return f"{symbol}{amount:,.2f}"

def format_date(dt: datetime, fmt: str = "%Y-%m-%d") -> str:
    """Format a datetime object as a string."""
    return dt.strftime(fmt)

def format_phone(number: str) -> str:
    """Format a 10-digit string as (XXX) XXX-XXXX."""
    digits = "".join(filter(str.isdigit, number))
    if len(digits) != 10:
        raise ValueError(f"Expected 10 digits, got {len(digits)}.")
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

def format_percentage(value: float, decimals: int = 1) -> str:
    """Format a float as a percentage string."""
    return f"{value:.{decimals}f}%"

def truncate(text: str, max_len: int = 80, suffix: str = "…") -> str:
    """Truncate text to max_len characters, appending suffix if cut."""
    if len(text) <= max_len:
        return text
    return text[: max_len - len(suffix)] + suffix

def pad_left(text: str, width: int, char: str = " ") -> str:
    """Left-pad text to the given width."""
    return text.rjust(width, char)