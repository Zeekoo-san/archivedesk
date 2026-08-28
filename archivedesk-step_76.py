# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: ArchiveDesk
import sys
from pathlib import Path

def handle_keyboard_interrupt():
    """Display a friendly message on Ctrl+C and exit cleanly."""
    print("\n\nInterrupted! Press Ctrl+C again to exit.", file=sys.stderr)
    sys.stdout.flush()
    sys.stderr.flush()

try:
    while True:
        try:
            input("ArchiveDesk> ")
        except KeyboardInterrupt:
            handle_keyboard_interrupt()
except KeyboardInterrupt:
    sys.exit(0)
