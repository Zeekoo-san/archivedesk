# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: ArchiveDesk
SETTINGS = {
    "archive_dir": "./archives",
    "retention_days": 365,
    "search_index_file": "./index.json",
    "audit_log_file": "./audit.log",
    "max_concurrent_searches": 4,
    "log_level": "INFO",
}


def get_setting(key: str):
    return SETTINGS.get(key)


def set_setting(key: str, value):
    if key not in SETTINGS:
        raise ValueError(f"Unknown setting: {key}")
    SETTINGS[key] = value
