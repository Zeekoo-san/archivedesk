# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: ArchiveDesk
def validate_required(value, field_name="field"):
    if value is None:
        raise ValueError(f"Required field '{field_name}' cannot be empty")
    return True

def validate_document_id(doc_id):
    if not doc_id or not isinstance(doc_id, str) or len(doc_id.strip()) == 0:
        raise ValueError("Document ID must be a non-empty string")
    if not re.match(r'^[A-Za-z0-9_\-]+$', doc_id.strip()):
        raise ValueError(f"Invalid document ID format: {doc_id}")
    return True

def validate_short_text(value, field_name="text", max_length=500):
    if value is None or not isinstance(value, str) or len(value.strip()) == 0:
        raise ValueError(f"{field_name} must be a non-empty string")
    if len(value.strip()) > max_length:
        raise ValueError(f"{field_name} exceeds maximum length of {max_length}")
    return True

def validate_date(value, field_name="date"):
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        raise ValueError(f"Invalid date format for {field_name}. Use YYYY-MM-DD")
