# === Stage 44: Add backup creation for the data file ===
# Project: ArchiveDesk
def backup_data(data_file, backup_dir=None):
    """Create a timestamped backup of the archive data file."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    src_path = Path(data_file).resolve()
    dst_path = Path(backup_dir) / f"archive_{ts}.bak"
    shutil.copy2(src_path, dst_path)
    print(f"Backup saved to {dst_path}")
