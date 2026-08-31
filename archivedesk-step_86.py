# === Stage 86: Add sample command transcripts for the main CLI workflows ===
# Project: ArchiveDesk
#!/usr/bin/env python3
"""Sample command transcripts for ArchiveDesk CLI workflows."""
from pathlib import Path

# ── Workflow 1: Create a Document with tags ──
# $ python archive_desk.py add --type=record --title="Quarterly Report Q1 2024" --body="Revenue summary for Q1" --tags="finance,quarterly" --retention=7yr
doc1 = {
    "id": "doc-001",
    "type": "record",
    "title": "Quarterly Report Q1 2024",
    "body": "Revenue summary for Q1",
    "tags": ["finance", "quarterly"],
    "retention": "7yr",
    "created_at": "2024-01-15T09:00:00Z",
}

# ── Workflow 2: Search documents by tag ──
# $ python archive_desk.py search --tag=finance --limit=10
search_query = {"query": "finance", "limit": 10, "sort": "recent"}

# ── Workflow 3: List audit history ──
# $ python archive_desk.py audit --since=2024-01-01 --type=modify
audit_query = {"since": "2024-01-01", "type": "modify"}

# ── Workflow 4: Retention compliance check ──
# $ python archive_desk.py retention --check=all --report=summary
retention_check = {"check": "all", "report": "summary"}

# ── Workflow 5: Export documents as JSON ──
# $ python archive_desk.py export --format=json --output=archive.json
export_config = {"format": "json", "output": "archive.json"}

# ── Workflow 6: Delete expired documents ──
# $ python archive_desk.py purge --expired=true --dry-run
purge_config = {"expired": True, "dry_run": True}
