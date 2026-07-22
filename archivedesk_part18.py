# === Stage 18: Add an activity log with timestamps and action names ===
# Project: ArchiveDesk
class ActivityLog:
    def __init__(self):
        self._log = []

    def log(self, action, entity_name=None, details=""):
        self._log.append({
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "entity": entity_name or "",
            "details": details
        })

    @property
    def entries(self):
        return self._log[:]
