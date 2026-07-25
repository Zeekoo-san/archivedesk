# === Stage 27: Add monthly summary calculations ===
# Project: ArchiveDesk
def monthly_summary(documents):
    """Compute per-month document counts, total size (bytes), and average retention days."""
    import collections
    month_counts = collections.defaultdict(int)
    month_total_size = collections.defaultdict(int)
    month_retention_days = collections.defaultdict(list)

    for doc in documents:
        m = doc.get("month", "unknown")
        size = doc.get("size_bytes", 0) or 0
        days = doc.get("retention_days", 0) or 0
        month_counts[m] += 1
        month_total_size[m] += size
        month_retention_days[m].append(days)

    result = {}
    for m in sorted(month_counts):
        avg_ret = (sum(month_retention_days[m]) / len(month_retention_days[m])) if month_retention_days[m] else 0
        result[m] = {
            "count": month_counts[m],
            "total_size_bytes": month_total_size[m],
            "avg_retention_days": round(avg_ret, 1)
        }
    return dict(result)
