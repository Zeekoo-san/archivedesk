# === Stage 20: Add duplicate detection for newly created records ===
# Project: ArchiveDesk
def detect_duplicate(self, new_record):
    """Check if a newly created record already exists (by title+date)."""
    key = (new_record.title.lower(), new_record.date)
    for r in self.records:
        if (r.title.lower() == key[0] and r.date == key[1]):
            return True, f"Duplicate of existing record '{r.id}'"
    return False, None
