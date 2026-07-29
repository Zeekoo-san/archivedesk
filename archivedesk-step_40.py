# === Stage 40: Add plain text report export ===
# Project: ArchiveDesk
def export_to_text(self, filename=None):
    if filename is None:
        filename = "archive_desk_report.txt"
    report_lines = []
    report_lines.append("ArchiveDesk Report")
    report_lines.append("=" * 40)
    for doc in self.documents.values():
        report_lines.append(f"\nDocument ID: {doc['id']}")
        report_lines.append(f"Title: {doc.get('title', 'N/A')}")
        report_lines.append(f"Tags: {', '.join(doc.get('tags', []))}")
        retention = doc.get("retention_rule", "None")
        report_lines.append(f"Retention Rule: {retention}")
    for rule in self.retention_rules.values():
        report_lines.append(f"\nRule Name: {rule['name']}")
        report_lines.append(f"Duration: {rule['duration']} years")
    if self.audit_log:
        report_lines.append("\nAudit Log:")
        for entry in self.audit_log[-10:]:
            report_lines.append(f"{entry['timestamp']}: {entry['action']} by {entry.get('user', 'unknown')}")
    with open(filename, "w") as f:
        f.write("\n".join(report_lines))
    return filename
