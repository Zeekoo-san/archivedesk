# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: ArchiveDesk
def delete_record(self, record_id: str, confirm: bool = False) -> dict:
    """Delete a record by ID with optional confirmation flag."""
    if record_id in self._records:
        record = self._records[record_id]
        audit_entry = AuditEntry(
            action="delete",
            record_id=record_id,
            user=self._user,
            timestamp=time.time(),
            details={"reason": "User confirmed" if confirm else "No confirmation"}
        )
        self._audit_log.append(audit_entry)
        del self._records[record_id]
        return {"status": "deleted", "record_id": record_id}

    raise KeyError(f"No record found with ID: {record_id}")
