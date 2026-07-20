# === Stage 14: Add file load support with fallback demo data ===
# Project: ArchiveDesk
def load_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"[Demo] File '{path}' not found; using built-in demo data.")
        return DEMO_DATA
