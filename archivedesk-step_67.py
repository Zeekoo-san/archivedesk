# === Stage 67: Add a function that returns key project metrics ===
# Project: ArchiveDesk
def project_metrics(archive):
    """Return key metrics for the ArchiveDesk project."""
    metrics = {}
    metrics['total_documents'] = len(archive.documents)
    metrics['total_tags'] = len(archive.tags)
    metrics['total_rules'] = len(archive.retention_rules)
    metrics['total_audit_records'] = len(archive.audit_log)
    metrics['active_documents'] = sum(1 for d in archive.documents.values() if not d.is_archived)
    metrics['archived_documents'] = sum(1 for d in archive.documents.values() if d.is_archived)
    metrics['retention_compliance'] = 0
    for rule in archive.retention_rules:
        if rule.is_compliant(archive):
            metrics['retention_compliance'] += 1
    metrics['retention_compliance'] = metrics['retention_compliance'] / len(archive.retention_rules) if len(archive.retention_rules) > 0 else 0.0
    metrics['search_indexed'] = archive.search_index is not None
    return metrics
