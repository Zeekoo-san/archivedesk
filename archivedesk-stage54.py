# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: ArchiveDesk
ANSI = {"reset": "\033[0m", "bold": "\033[1m", "dim": "\033[2m",
        "red": "\033[31m", "green": "\033[32m", "yellow": "\033[33m",
        "blue": "\033[34m", "cyan": "\033[36m", "white": "\033[37m"}

def colorize(text, color):
    return f"{ANSI[color]}{text}{ANSI['reset']}" if text else ""
