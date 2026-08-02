# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: ArchiveDesk
def _format_date(value, fmt="%Y-%m-%d"):
    """Return a date value formatted as *fmt*; fall back to str() if it isn't a datetime."""
    try:
        from datetime import datetime as _dt
        if isinstance(value, _dt):
            return value.strftime(fmt)
    except Exception:
        pass
    return str(value)


def _safe_int(value, default=0):
    """Convert *value* to int; return *default* on failure."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _strip_tags(raw):
    """Remove HTML-style tags from a string and collapse whitespace."""
    import re
    cleaned = re.sub(r"<[^>]+>", "", raw)
    return " ".join(cleaned.split())
