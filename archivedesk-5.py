# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: ArchiveDesk
def update_document(self, doc_id: str, **fields) -> dict | None:
    """Update a document by ID; return updated record or None if missing."""
    rec = self._find(doc_id)
    if rec is None:
        raise ValueError(f"Document '{doc_id}' not found")
    for key, value in fields.items():
        if key in ("id", "audit_log"):
            continue  # never overwrite identity or history externally
        setattr(rec, key, value)

    audit = AuditEntry(
        action="update", record_id=doc_id,
        timestamp=datetime.now(timezone.utc),
        changed_fields=list(fields.keys()),
    )
    rec.audit_log.insert(0, audit)
    if len(rec.audit_log) > MAX_AUDIT_PER_DOC:
        rec.audit_log = rec.audit_log[:MAX_AUDIT_PER_DOC]

    self._persist()
    return dict(rec)
