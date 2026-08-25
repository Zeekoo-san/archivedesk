# === Stage 66: Add export of a short status dashboard ===
# Project: ArchiveDesk
def status_dashboard(records, tags, rules, audit_log, config):
    """Generate a compact status dashboard from the archive desk state."""
    total = len(records)
    active = sum(1 for r in records if r["status"] == "active")
    archived = sum(1 for r in records if r["status"] == "archived")
    expired = sum(1 for r in records if r["status"] == "expired")
    retention_count = sum(1 for r in records if r["status"] == "retained")
    tag_count = len(tags)
    rule_count = len(rules)
    audit_count = len(audit_log)
    retention_pct = (retention_count / total * 100) if total > 0 else 0
    expiry_pct = (expired / total * 100) if total > 0 else 0
    dashboard = {
        "total_records": total,
        "active": active,
        "archived": archived,
        "expired": expired,
        "retained": retention_count,
        "retention_pct": round(retention_pct, 1),
        "expiry_pct": round(expiry_pct, 1),
        "tags": tag_count,
        "rules": rule_count,
        "audit_entries": audit_count
    }
    return dashboard
