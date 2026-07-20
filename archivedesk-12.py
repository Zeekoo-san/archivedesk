# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: ArchiveDesk
def import_json(path):
    """Import records from a JSON file with friendly error handling."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict):
            return [data]
        if not isinstance(data, list):
            raise ValueError("JSON root must be an array or a single object")
        records = []
        for item in data:
            if not isinstance(item, dict):
                raise ValueError(f"Expected an object at index {len(records)}, got {type(item).__name__}")
            records.append(item)
        return records
    except FileNotFoundError:
        print(f"[ArchiveDesk] File not found: {path}")
        return []
    except json.JSONDecodeError as e:
        print(f"[ArchiveDesk] Malformed JSON in {path}: {e}")
        return []
    except ValueError as e:
        print(f"[ArchiveDesk] Import error – {e}")
        return []
