from dataclasses import asdict, dataclass
from typing import List


@dataclass
class LogEntry:
    id: str
    message: str
    tags: List[str]
    created_at: str

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "LogEntry":
        return cls(
            id=data["id"],
            message=data["message"],
            tags=data.get("tags", []),
            created_at=data["created_at"],
        )