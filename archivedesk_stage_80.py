# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: ArchiveDesk
def format_document_entry(doc: dict) -> str:
    """Return a single-line, human-readable summary of a document."""
    parts = [f"Document: {doc['id']}"]
    if doc.get("title"):
        parts.append(f"Title: {doc['title']}")
    if doc.get("created_at"):
        parts.append(f"Created: {doc['created_at']}")
    if doc.get("retention_rule_id"):
        parts.append(f"Retention: {doc['retention_rule_id']}")
    if doc.get("status") not in ("pending", "unknown"):
        parts.append(f"Status: {doc['status']}")
    return " | ".join(parts)


def format_audit_entry(entry: dict) -> str:
    """Return a single-line, human-readable summary of an audit event."""
    parts = [f"Audit: {entry['id']}"]
    if entry.get("user") and entry["user"]:
        parts.append(f"User: {entry['user']}")
    if entry.get("action") and entry["action"]:
        parts.append(f"Action: {entry['action']}")
    if entry.get("timestamp"):
        parts.append(f"Time: {entry['timestamp']}")
    return " | ".join(parts)


def format_rule_entry(rule: dict) -> str:
    """Return a single-line, human-readable summary of a retention rule."""
    parts = [f"Rule: {rule['id']}"]
    if rule.get("name"):
        parts.append(f"Name: {rule['name']}")
    if rule.get("retention_period") is not None:
        parts.append(f"Retention: {rule['retention_period']}")
    if rule.get("status") not in ("pending", "unknown"):
        parts.append(f"Status: {rule['status']}")
    return " | ".join(parts)
