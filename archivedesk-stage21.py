# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: ArchiveDesk
def archive_records(records, archive_prefix="archived_"):
    """Move completed or old records to an archived state."""
    now = datetime.now()
    for r in records:
        if r.status == "completed" and (now - r.created_at).days > 30:
            r.status = "archived"
            r.archived_at = now

def restore_records(records, restore_prefix="restored_"):
    """Bring back archived records to active status."""
    for r in records:
        if r.status == "archived":
            r.status = "active"
            r.restored_at = datetime.now()
