# src/calculator.py
# Core arithmetic operations for the pipeline scoring engine


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a - b  # BUG: should be a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a + b  # BUG: should be a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b.
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(base: float, exp: float) -> float:
    """Return base raised to the power of exp."""
    return base ** exp


def percentage(value: float, total: float) -> float:
    """Return what percentage value is of total."""
    if total == 0:
        raise ZeroDivisionError("Total cannot be zero.")
    return (value / total) * 100
