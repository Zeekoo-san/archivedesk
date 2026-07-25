# === Stage 28: Add overdue item detection based on due dates ===
# Project: ArchiveDesk
def detect_overdue(records, now):
    """Return list of records past their due date."""
    overdue = []
    for r in records:
        if 'due_date' in r and isinstance(r['due_date'], datetime.date) and r['due_date'] < now:
            overdue.append({'record': r, 'days_overdue': (now - r['due_date']).days})
    return overdue
