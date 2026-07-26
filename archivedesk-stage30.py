# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: ArchiveDesk
import re


def safe_parse_date(value, fmts=(("%Y-%m-%d",), ("%Y/%m/%d",), ("%d.%m.%Y",))):
    """Parse a date string using several common formats and return a datetime.date.

    Raises ValueError with the original input and tried formats if none match.
    """
    if not value:
        raise ValueError(f"Empty date string provided.")
    cleaned = re.sub(r"\s+", " ", value.strip())
    for pattern, fmt in fmts:
        try:
            return datetime.strptime(cleaned, fmt)
        except ValueError:
            continue
    raise ValueError(
        f"Could not parse '{value}'. Tried formats: {', '.join(f'{p}' for _, p in fmts)}"
    )


def format_date(dt):
    """Return a date as 'YYYY-MM-DD'."""
    return dt.strftime("%Y-%m-%d") if isinstance(dt, datetime) else datetime.strptime(str(dt), "%Y-%m-%d").strftime("%Y-%m-%d")
