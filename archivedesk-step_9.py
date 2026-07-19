# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: ArchiveDesk
def sort_records(records, key="title", ascending=True):
    """Sort archive records by title, date, priority, or last update."""
    if key == "priority":
        return sorted(records, key=lambda r: (r.priority is None and 1 or 0), reverse=not ascending)
    elif key == "last_update":
        def updater(r):
            d = r.last_update.isoformat() if hasattr(r.last_update, 'isoformat') else str(r.last_update)
            return d if d != "" else "9999-12-31"
        return sorted(records, key=updater, reverse=not ascending)
    elif key == "date":
        def datr(r):
            d = r.date.isoformat() if hasattr(r.date, 'isoformat') else str(r.date)
            return d if d != "" else "9999-12-31"
        return sorted(records, key=datr, reverse=not ascending)
    elif key == "title":
        def title_lower(r):
            t = r.title or ""
            return (t.lower(), t[::-1]) if t else ("", "")
        return sorted(records, key=title_lower, reverse=not ascending)
    else:
        return sorted(records, key=lambda r: getattr(r, key, ""), reverse=not ascending)
