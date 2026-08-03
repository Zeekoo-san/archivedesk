# === Stage 58: Add bulk update behavior for selected records ===
# Project: ArchiveDesk
def bulk_update_records(self, record_ids: list[str], updates: dict):
    """Apply a single update action to every record in `record_ids` that still exists."""
    updated = []
    for rid in record_ids:
        rec = self._cache.get(rid)
        if rec is None:
            continue  # silently skip deleted records
        new_state = dict(rec.state)
        merged = merge_update(new_state, updates)
        if merged != new_state:
            rec.state = merged
            updated.append(rid)
    self._cache.set_batch(updated, lambda _: None)  # state is already mutated in-place
    return {rid: self._record_to_dict(rec) for rid in updated}
