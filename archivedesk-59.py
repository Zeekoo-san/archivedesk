# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: ArchiveDesk
def bulk_delete_with_confirmation(records, confirm_flag=True):
    """Delete multiple records only when user confirms via flag."""
    if not confirm_flag:
        print("Bulk delete cancelled by user.")
        return 0
    deleted_count = 0
    for record in records:
        archive_desk.delete_record(record.id)
        deleted_count += 1
        print(f"Deleted record ID: {record.id}")
    print(f"Bulk delete complete. Total deleted: {deleted_count}")
    return deleted_count
