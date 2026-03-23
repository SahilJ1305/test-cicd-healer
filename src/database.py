# src/database.py
# Lightweight database manager for storing pipeline run records

import json
import os
import uuid
from datetime import datetime

class DatabaseManager:
    """Simple file-backed JSON database for run records."""

    def __init__(self, filepath: str = "runs.json"):
        self.filepath = filepath
        self._records: dict = {}
        self._load()

    def _load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                self._records = json.load(f)

    def _save(self):
        with open(self.filepath, "w") as f:
            json.dump(self._records, f, indent=2)

    def insert(self, data: dict) -> str:
        """Insert a record and return its generated ID."""
        record_id = str(uuid.uuid4())
        self._records[record_id] = {
            **data,
            "id":         record_id,
            "created_at": datetime.utcnow().isoformat(),
        }
        self._save()
        return record_id

    def get(self, record_id: str) -> dict:
        """Fetch a record by ID. Returns None if not found."""
        return self._records.get(record_id)

    def all(self) -> list:
        """Return all stored records as a list."""
        return list(self._records.values())

    def delete(self, record_id: str) -> bool:
        """Delete a record by ID. Returns True if deleted."""
        if record_id in self._records:
            del self._records[record_id]
            self._save()
            return True
        return False

    def count(self) -> int:
        """Return the number of stored records."""
        return len(self._records)

def get_user(user_id: str) -> dict:
    """Fetch a user by ID. Returns None if not found."""
    db = DatabaseManager()
    return db.get(user_id)

def save_user(user_data: dict) -> str:
    """Save a user record and return its generated ID."""
    db = DatabaseManager()
    return db.insert(user_data)

def delete_user(user_id: str) -> bool:
    """Delete a user by ID. Returns True if deleted."""
    db = DatabaseManager()
    return db.delete(user_id)