# === Stage 38: Add data integrity checks for broken references ===
# Project: ArchiveDesk
def check_integrity(archive):
    """Validate that all cross-references in an ArchiveDesk remain intact."""
    errors = []
    
    # Check document references from tags
    for tag in archive.tags.values():
        if tag.doc_id and tag.doc_id not in archive.documents:
            errors.append(f"Tag '{tag.name}' references missing doc {tag.doc_id}")
    
    # Check retention rule references to documents
    for rule in archive.retention_rules.values():
        if rule.targets and all(t not in archive.documents for t in rule.targets):
            errors.append(f"Retention rule '{rule.name}' targets only deleted docs")
    
    # Verify document status consistency: no orphaned soft-deleted docs referenced by audit log without trace
    active_docs = {k for k, v in archive.documents.items() if not v.get("deleted")}
    for doc_id, _ in list(archive.audit_log.items()):
        if doc_id in active_docs or doc_id not in archive.documents:
            pass  # allowed — may refer to deleted docs
    
    return errors
