# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: ArchiveDesk
def clear_archive(state: dict) -> dict:
    """Clear all documents, tags, rules, search history, and audit log after confirmation."""
    if not state.get("confirm_clear", False):
        raise RuntimeError("No confirmation flag set; call confirm_clear() first.")
    state["documents"] = {}
    state["tags"] = {}
    state["rules"] = []
    state["search_history"] = []
    state["audit_log"] = []
    state["confirm_clear"] = False
    state["last_action"] = "archive_cleared"
    return state
