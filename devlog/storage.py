import json
from pathlib import Path
from typing import List

from .models import LogEntry


class JsonStorage:
    def __init__(self, path: str = "devlog.json"):
        self.path = Path(path)

    def load(self) -> List[LogEntry]:
        if not self.path.exists():
            return []

        with self.path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return [LogEntry.from_dict(item) for item in data]

    def save(self, entries: List[LogEntry]) -> None:
        data = [entry.to_dict() for entry in entries]

        with self.path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)