from datetime import datetime, timezone
from uuid import uuid4

from .models import LogEntry
from .storage import JsonStorage


class DevLogService:
    def __init__(self, storage: JsonStorage):
        self.storage = storage

    def add_entry(self, message: str, tags=None) -> LogEntry:
        if not message.strip():
            raise ValueError("Message cannot be empty.")

        tags = tags or []

        entry = LogEntry(
            id=str(uuid4())[:8],
            message=message.strip(),
            tags=tags,
            created_at=datetime.now(timezone.utc).isoformat(),
        )

        entries = self.storage.load()
        entries.append(entry)

        self.storage.save(entries)

        return entry

    def list_entries(self):
        return self.storage.load()

    def delete_entry(self, entry_id: str) -> bool:
        entries = self.storage.load()

        filtered_entries = [
            entry
            for entry in entries
            if entry.id != entry_id
        ]

        if len(entries) == len(filtered_entries):
            return False

        self.storage.save(filtered_entries)

        return True