# === Stage 46: Add a schema version field and migration helper ===
# Project: ArchiveDesk
SCHEMA_VERSION = 1


def migrate_to(version):
    """Apply schema migrations up to the target version."""
    global SCHEMA_VERSION
    if SCHEMA_VERSION < version:
        print(f"Migrating schema from {SCHEMA_VERSION} to {version}")
        # Placeholder for future migration logic
        pass
    else:
        print(f"Schema already at version {SCHEMA_VERSION}, skipping migration")
    SCHEMA_VERSION = version
