# === Stage 64: Add validation for relationship references ===
# Project: ArchiveDesk
class ValidationError(Exception):
    pass

class ReferentialIntegrityError(ValidationError):
    pass

def validate_relationship_references(records, table_name):
    """Validate that all foreign key references in the given table are valid."""
    if table_name not in records:
        raise ReferentialIntegrityError(
            f"Table '{table_name}' not found in records"
        )
    if not records[table_name]:
        return
    for record in records[table_name]:
        for field, value in record.items():
            if isinstance(value, dict):
                ref = value.get('ref')
                if ref:
                    ref_table = value.get('table')
                    if ref_table and ref_table not in records:
                        raise ReferentialIntegrityError(
                            f"Reference to table '{ref_table}' in field '{field}' "
                            f"is invalid for record {record.get('id', 'unknown')}"
                        )
    return "All relationship references are valid"
