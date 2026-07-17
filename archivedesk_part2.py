# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: ArchiveDesk
from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Tag:
    name: str
    color: str = "#555"
    description: str = ""

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, Tag):
            return self.name == other.name
        return NotImplemented


@dataclass
class RetentionRule:
    tag_name: str
    retention_days: int
    auto_archive: bool = False
    expires_after: date | None = None

    def is_expired(self) -> bool:
        if self.expires_after is not None:
            return date.today() >= self.expires_after
        return date.today() > (date.today() + timedelta(days=self.retention_days))


@dataclass
class AuditEntry:
    timestamp: str = field(default_factory=lambda: __import__("datetime").datetime.now().isoformat())
    action: str  # "created", "archived", "deleted"
    record_id: int | None = None
    user: str = "system"
