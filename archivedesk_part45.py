# === Stage 45: Add restore from backup with validation ===
# Project: ArchiveDesk
def restore_backup(archive_path, backup_file):
    """Restore a backup zip/tar to archive_path with validation."""
    import zipfile, tarfile, os, shutil
    if not os.path.exists(os.path.join(archive_path, "documents")):
        raise FileNotFoundError("Archive desk is empty; no documents directory found.")
    target = os.path.join(archive_path)
    try:
        if backup_file.endswith(".zip"):
            with zipfile.ZipFile(backup_file, "r") as z:
                for info in z.infolist():
                    if info.is_dir(): continue
                    path = os.path.join(target, info.filename.lstrip("/"))
                    if not path.startswith(target): raise ValueError("Unauthorized file in backup.")
                    z.extract(info, target)
        elif backup_file.endswith((".tar.gz", ".tgz")):
            with tarfile.open(backup_file, "r:*") as t:
                for m in t.getmembers():
                    if not m.name.startswith(target): raise ValueError("Unauthorized file in backup.")
                    t.extract(m, target)
        else:
            raise ValueError(f"Unsupported backup format: {os.path.basename(backup_file)}")
    except zipfile.BadZipFile as e:
        raise RuntimeError("Corrupt zip backup detected") from e
    shutil.rmtree(target, ignore_errors=True)
    os.makedirs(os.path.join(target, "documents"), exist_ok=True)
    os.makedirs(os.path.join(target, "audit_log"), exist_ok=True)
    return f"Backup restored to {target}"
