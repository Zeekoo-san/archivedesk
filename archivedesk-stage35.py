# === Stage 35: Add active user switching and user-specific records ===
# Project: ArchiveDesk
from typing import Optional, Dict, List


class UserSession:
    def __init__(self):
        self._active_user: Optional[str] = None
        self._user_records: Dict[str, List[Record]] = {}
        self._users: Dict[str, str] = {}

    @property
    def active_user(self) -> Optional[str]:
        return self._active_user

    @active_user.setter
    def active_user(self, value: str):
        if value not in self._users:
            raise ValueError(f"User '{value}' is not registered")
        self._active_user = value
        if value not in self._user_records:
            self._user_records[value] = []

    @property
    def user_records(self) -> List[Record]:
        u = self.active_user
        return list(self._user_records.get(u, [])) if u else []

    def add_record_for_current_user(self, record: Record):
        u = self.active_user
        if not u:
            raise RuntimeError("No active user set")
        self._user_records[u].append(record)
