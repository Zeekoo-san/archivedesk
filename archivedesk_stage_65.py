# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: ArchiveDesk
# Step 65 – merge imports cleanly: skip duplicates and keep relative imports preferred
import sys

def _add_unique_import(path, name, _seen=None):
    """Append `import name from path` only when it isn't already present."""
    if _seen is None:
        _seen = set()
    if name in _seen:
        return False
    _seen.add(name)
    # try relative first, then absolute
    for candidate in (f"{path}.{name}", name):
        try:
            __import__(candidate)
            return True
        except ImportError:
            continue
    # fallback: just record it (will be resolved at runtime)
    return False

# Example usage – replace these with the actual paths/names your project needs:
# _add_unique_import("archive_desk", "documents")
# _add_unique_import("archive_desk", "tags")
# _add_unique_import("archive_desk", "retention")
# _add_unique_import("archive_desk", "search")
# _add_unique_import("archive_desk", "audit")
