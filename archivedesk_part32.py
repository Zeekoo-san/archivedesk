# === Stage 32: Add pagination helpers for long console output ===
# Project: ArchiveDesk
def paginate(lines, per_page=50):
    """Yield chunks of `lines` for console pagination."""
    import sys
    chunk = lines[:per_page]
    while chunk:
        print('\n'.join(chunk))
        if len(chunk) < len(lines):
            sys.stdout.write('Scroll down to see more...\n')
            sys.stdout.flush()
        chunk = lines[per_page:]
