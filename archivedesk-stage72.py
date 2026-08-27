# === Stage 72: Add Markdown report export ===
# Project: ArchiveDesk
def export_markdown_report(records, output_path=None):
    """Export a Markdown report of all records to a file."""
    lines = [
        "# ArchiveDesk Report",
        f"Generated: {datetime.datetime.now().isoformat()}",
        "",
        "## Documents",
        "",
    ]
    for doc in records:
        tags = ", ".join(doc.get("tags", []))
        lines.append(f"- **{doc['id']}**: {doc.get('title', 'untitled')} | Tags: {tags} | Date: {doc.get('date', 'N/A')}")
    lines.append("")
    return "\n".join(lines)
