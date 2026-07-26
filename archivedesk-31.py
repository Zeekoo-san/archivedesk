# === Stage 31: Add compact table rendering for long lists ===
# Project: ArchiveDesk
def render_compact_table(rows, columns):
    """Render a compact table from rows and column names."""
    if not rows:
        return ""
    col_widths = [len(c) for c in columns]
    for row in rows:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val)))
    lines = []
    sep = " | ".join("-" * w for w in col_widths)
    header = " | ".join(columns)
    lines.append(header)
    lines.append(sep)
    for row in rows:
        line = " | ".join(str(v).ljust(w) for v, w in zip(row, col_widths))
        lines.append(line)
    return "\n".join(lines)
