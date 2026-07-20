# === Stage 11: Add JSON export for the current application state ===
# Project: ArchiveDesk
import json, datetime

def export_state(app):
    state = {
        "documents": [{"id": d["id"], "title": d["title"], "tag_ids": d["tag_ids"]} for d in app["documents"]],
        "tags": list(app["tags"].items()),
        "retention_rules": list(app["retention_rules"].items()),
        "audit_log": [{"action": a[0], "timestamp": str(a[1]), "detail": a[2]} for a in app["audit_log"]],
        "last_exported": datetime.datetime.now().isoformat()
    }
    return json.dumps(state, indent=2)
