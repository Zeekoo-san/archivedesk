# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: ArchiveDesk
def generate_validation_report(documents, rules, tags):
    warnings = []
    errors = []
    for doc in documents:
        if doc.get('expiry_date'):
            if datetime.now() > datetime.strptime(doc['expiry_date'], '%Y-%m-%d'):
                errors.append(f"Document '{doc['title']}' has expired on {doc['expiry_date']}.")
        if not doc.get('filename'):
            warnings.append(f"Document '{doc['title']}' is missing a filename.")
        if not doc.get('created_at'):
            warnings.append(f"Document '{doc['title']}' has no creation timestamp.")
        if doc.get('tags'):
            for tag in doc['tags']:
                if tag not in tags:
                    warnings.append(f"Document '{doc['title']}' uses unknown tag '{tag}'.")
    return {'warnings': warnings, 'errors': errors}
