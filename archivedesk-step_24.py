# === Stage 24: Add grouped summaries by category or status ===
# Project: ArchiveDesk
def grouped_summary(records, group_by=None):
    if group_by is None:
        group_by = 'status'
    groups = {}
    for r in records:
        key = r.get(group_by, 'Unknown')
        groups.setdefault(key, {'count': 0, 'total_age_days': 0})
        groups[key]['count'] += 1
        if hasattr(r, 'created_at'):
            import datetime as _d
            age = (_d.date.today() - r.created_at).days
            groups[key]['total_age_days'] += age
    return {k: {'count': v['count'], 'avg_age_days': round(v['total_age_days'] / max(v['count'], 1))} for k, v in groups.items()}
