# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: ArchiveDesk
def diff_records(before, after):
    """Compare two record states and return a list of changed fields."""
    if not isinstance(before, dict) and not isinstance(after, dict):
        return str(before) != str(after)
    changes = []
    all_keys = set(before.keys()) | set(after.keys())
    for key in sorted(all_keys):
        if before.get(key) != after.get(key):
            changes.append((key, before.get(key), after.get(key)))
    return changes
