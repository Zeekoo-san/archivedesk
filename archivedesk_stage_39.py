# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: ArchiveDesk
def repair_simple_integrity(archive_data):
    """Repair basic data integrity issues in ArchiveDesk."""
    if isinstance(archive_data, dict) and 'documents' in archive_data:
        docs = archive_data['documents']
        for i, doc in enumerate(docs):
            if not isinstance(doc, dict) or 'id' not in doc:
                doc['id'] = f"doc_{i}"
            if not isinstance(doc.get('tags'), list):
                doc['tags'] = []
            if not isinstance(doc.get('created_at', ''), str) and doc.get('created_at') is not None:
                import datetime
                doc['created_at'] = datetime.datetime.now().isoformat()
        archive_data['documents'] = docs
    elif isinstance(archive_data, list):
        for i, item in enumerate(archive_data):
            if not isinstance(item, dict) or 'id' not in item:
                item['id'] = f"item_{i}"
