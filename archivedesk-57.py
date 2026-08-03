# === Stage 57: Add structured result objects for command handlers ===
# Project: ArchiveDesk
class ArchiveResult:
    """Compact structured result for archive command handlers."""
    def __init__(self, status: str, message: str = "", data=None):
        self.status = status  # 'ok' | 'error' | 'warning'
        self.message = message
        self.data = data

    @property
    def is_ok(self) -> bool:
        return self.status == "ok"

    @property
    def is_error(self) -> bool:
        return self.status == "error"

    def to_dict(self) -> dict:
        result = {"status": self.status, "message": self.message}
        if self.data is not None:
            result["data"] = self.data
        return result

    def __repr__(self):
        return f"<ArchiveResult status={self.status!r}>"
