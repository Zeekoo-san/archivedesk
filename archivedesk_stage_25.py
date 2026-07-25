# === Stage 25: Add daily summary calculations ===
# Project: ArchiveDesk
def daily_summary(records):
    """Compute a compact daily summary for each calendar day."""
    from collections import defaultdict
    by_day = defaultdict(lambda: {"count": 0, "total_size": 0})
    for doc in records:
        d = doc.get("created_at") or doc.get("updated_at", "")[:10]
        if not d:
            continue
        by_day[d]["count"] += 1
        try:
            size = int(doc.get("size", 0))
            by_day[d]["total_size"] += size
        except (TypeError, ValueError):
            pass
    return [{"date": k, **v} for k, v in sorted(by_day.items())]
