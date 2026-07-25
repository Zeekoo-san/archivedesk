# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: ArchiveDesk
def upcoming_items(records, days_ahead=365):
    """Return records whose end_date is within `days_ahead` of today."""
    from datetime import date, timedelta
    now = date.today()
    cutoff = now + timedelta(days=days_ahead)
    return [r for r in records if isinstance(r.get("end_date"), date) and r["end_date"] <= cutoff]

def reminders(records):
    """Return records whose end_date is on or before today (overdue)."""
    from datetime import date, timedelta
    now = date.today() + timedelta(days=1)
    return [r for r in records if isinstance(r.get("end_date"), date) and r["end_date"] <= now]
