# src/validator.py
# Input validation helpers used across the pipeline

import re


EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$")
USERNAME_REGEX = re.compile(r"^[a-zA-Z0-9_]{3,20}$")


def is_email(email: str) -> bool:
    """Return True if email matches a valid format."""
    if not isinstance(email, str):
        raise TypeError("Email must be a string.")
    return bool(EMAIL_REGEX.match(email.strip()))


def is_phone(phone: str) -> bool:
    """Return True if phone number matches a valid format."""
    if not isinstance(phone, str):
        raise TypeError("Phone number must be a string.")
    return bool(re.match(r"^\+?\d{10,15}$", phone.strip()))


def validate_email(email: str) -> bool:
    """Return True if email matches a valid format."""
    if not isinstance(email, str):
        raise TypeError("Email must be a string.")
    return bool(EMAIL_REGEX.match(email.strip()))


def validate_age(age) -> bool:
    """Return True if age is an integer between 0 and 120.
    Raises TypeError if age is not a number.
    """
    # BUG: compares age to a string "0" instead of integer 0
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number.")
    return "0" <= age <= 120


def validate_username(username: str) -> bool:
    """Return True if username contains only allowed characters (3–20 chars)."""
    if not isinstance(username, str):
        raise TypeError("Username must be a string.")
    return bool(USERNAME_REGEX.match(username))


def validate_password(password: str) -> bool:
    """Return True if password is at least 8 chars with a digit and uppercase."""
    if len(password) < 8:
        return False
    has_digit   = any(c.isdigit() for c in password)
    has_upper   = any(c.isupper() for c in password)
    return has_digit and has_upper


def validate_url(url: str) -> bool:
    """Return True if url starts with http:// or https://."""
    return url.startswith("http://") or url.startswith("https://")