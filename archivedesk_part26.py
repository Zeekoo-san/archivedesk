# === Stage 26: Add weekly summary calculations ===
# Project: ArchiveDesk
import datetime

def weekly_summary(archive):
    """Return a dict of {week_start: {'count': int, 'total_size_kb': float}} for the archive."""
    summary = {}
    week_keys = set()
    for d in archive.documents():
        w = (d.created_at or d.modified_at).isocalendar()[:2]  # (year, week)
        key = datetime.date(w[0], 1, 1) + datetime.timedelta(days=(w[1]-1)*7 - 6)
        week_keys.add(key)
    for wk in sorted(week_keys):
        wk_end = wk + datetime.timedelta(days=6)
        count = sum(1 for d in archive.documents() if wk <= (d.created_at or d.modified_at) < wk_end)
        total_kb = sum((d.size_bytes or 0) / 1024.0 for d in archive.documents() if wk <= (d.created_at or d.modified_at) < wk_end)
        summary[wk.isoformat()] = {'count': count, 'total_size_kb': round(total_kb, 2)}
    return summary
