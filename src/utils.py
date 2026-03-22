# src/utils.py
# General-purpose helper utilities

from typing import Any, List, Optional

def flatten_list(nested: list) -> list:
    """Recursively flatten a nested list into a single list."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def chunk_list(lst: list, size: int) -> list:
    """Split a list into chunks of the given size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    return [lst[i : i + size] for i in range(0, len(lst), size)]

def safe_get(d: dict, *keys, default: Any = None) -> Any:
    """Safely traverse nested dicts without raising KeyError."""
    current = d
    for key in keys:
        if not isinstance(current, dict):
            return default
        current = current.get(key, default)
        if current is default:
            return default
    return current

def deduplicate(lst: list) -> list:
    """Return a list with duplicates removed, preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def merge_dicts(*dicts: dict) -> dict:
    """Merge multiple dicts left-to-right (later keys win)."""
    result = {}
    for d in dicts:
        result.update(d)
    return result