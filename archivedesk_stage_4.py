# === Stage 4: Implement create operations for the primary records ===
# Project: ArchiveDesk
def create_document(record_id, title, content, owner="archive_user", tags=None):
    """Create a new document record."""
    if tags is None:
        tags = []
    metadata = {
        "title": title,
        "content": content,
        "owner": owner,
        "created_at": datetime.now().isoformat(),
        "tags": tags,
    }
    return Document(record_id=record_id, **metadata)

def create_tag(tag_name):
    """Create a new tag record."""
    if not tag_name:
        raise ValueError("Tag name must be non-empty")
    return Tag(tag_name=tag_name)

def create_retention_rule(rule_name, min_age_days, action="delete", status="active"):
    """Create a retention rule for documents by age."""
    return RetentionRule(
        rule_name=rule_name,
        min_age_days=min_age_days,
        action=action,
        status=status,
        created_at=datetime.now().isoformat(),
    )

def create_audit_entry(entry_id, user, action, record_type="document", details=None):
    """Create an audit history entry."""
    if details is None:
        details = {}
    return AuditEntry(
        entry_id=entry_id,
        user=user,
        action=action,
        record_type=record_type,
        details=details,
        timestamp=datetime.now().isoformat(),
    )
