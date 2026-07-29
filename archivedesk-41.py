# === Stage 41: Add plain text import for a simple line-based format ===
# Project: ArchiveDesk
def import_lines(self, text: str) -> int:
    """Import documents from a simple line-based format."""
    lines = [l.strip() for l in text.splitlines()] if text else []
    count = 0
    for line in lines:
        if not line or line.startswith('#'):
            continue
        parts = line.split('\t', 2)
        if len(parts) < 3:
            parts += [''] * (3 - len(parts))
        doc_id, title, body = parts[:3]
        tag_str = parts[3].strip() if len(parts) > 3 else ''
        tags = [t.strip() for t in tag_str.split(';') if t.strip()] if tag_str else []
        self.add_document(doc_id=doc_id, title=title, body=body, tags=tags)
        count += 1
    return count
