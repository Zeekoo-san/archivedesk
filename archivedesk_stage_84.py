# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: ArchiveDesk
def _cleanup(self):
        """Remove stale helpers and duplicate logic."""
        for fn in ['_sanitize', '_to_json', '_validate']:
            if hasattr(self, fn):
                delattr(self, fn)
        if hasattr(self, 'duplicate_check'):
            delattr(self, 'duplicate_check')
        return self
