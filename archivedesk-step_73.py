# === Stage 73: Add a lightweight HTML report export ===
# Project: ArchiveDesk
import html

def export_report(records, output_file):
    """Generate a lightweight HTML report from archive records."""
    lines = ["<html><head><title>ArchiveDesk Report</title>",
             "<style>table{border-collapse:collapse;width:100%%}th,td{border:1px solid #ddd;padding:8px}th{background:#f4f4f4}</style>",
             "</head><body><h1>ArchiveDesk Report</h1><table><tr><th>ID</th><th>Title</th><th>Tags</th><th>Retained</th></tr>"]
    for r in records:
        tags = ",".join(r.get("tags", []))
        lines.append(f"<tr><td>{r['id']}</td><td>{html.escape(r['title'])}</td><td>{html.escape(tags)}</td><td>{r.get('retained', False)}</td></tr>")
    lines.append("</table></body></html>")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
