# === Stage 42: Add CSV export without external dependencies ===
# Project: ArchiveDesk
import csv
from io import StringIO


def export_to_csv(records, fieldnames):
    """Export a list of record dicts to a CSV string without external dependencies."""
    buf = StringIO()
    writer = csv.DictWriter(buf, fieldnames=fieldnames)
    writer.writeheader()
    for rec in records:
        writer.writerow({k: rec.get(k, "") for k in fieldnames})
    return buf.getvalue()
