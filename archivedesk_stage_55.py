# === Stage 55: Add a setting to disable colorized output ===
# Project: ArchiveDesk
import sys


def disable_color_output():
    """Disable colorized output if the terminal does not support it."""
    try:
        import curses
        curses.setupterm()
        curses.endwin()
        has_colors = curses.tigetnum("colors") > 1
    except Exception:
        has_colors = sys.stdout.isatty()

    if not has_colors:
        print("\033[39m", end="")
