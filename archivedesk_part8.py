# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: ArchiveDesk
def filter_records(records, status=None, category=None, owner=None, tag=None):
    """Filter records by optional status, category, owner, and/or tag."""
    filtered = records
    if status is not None:
        filtered = [r for r in filtered if r.get('status') == status]
    if category is not None:
        filtered = [r for r in filtered if r.get('category') == category]
    if owner is not None:
        filtered = [r for r in filtered if r.get('owner') == owner]
    if tag is not None:
        filtered = [r for r in filtered if tag in r.get('tags', [])]
    return filtered
