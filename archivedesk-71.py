# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: ArchiveDesk
def seed_demo_data(db):
    """Insert a small set of deterministic sample records."""
    from datetime import datetime, timedelta
    now = datetime(2024, 6, 15)
    for i, name in enumerate(["Invoice_001", "Invoice_002", "Memo_001", "Contract_001"], start=1):
        doc = {
            "id": f"doc-{i:03d}",
            "title": name,
            "content": f"Sample content for {name} – generated at {now}",
            "created_at": now - timedelta(days=i * 3),
            "updated_at": now - timedelta(days=i),
            "tags": ["demo", "sample", "archive"] if i != 2 else ["demo", "urgent"],
            "retention_rule": "7_years",
            "status": "active" if i != 3 else "archived",
            "author": "system",
        }
        db["documents"].insert_one(doc)
    for i, rule in enumerate([("7_years", "2020-01-01"), ("3_years", "2022-01-01"), ("forever", "2024-01-01")]):
        db["retention_rules"].insert_one({"id": f"rule-{i+1:03d}", "name": rule[0], "effective_date": rule[1], "status": "active"})
    db["audit_log"].insert_one({"id": "audit-001", "action": "seed_demo", "user": "system", "timestamp": now, "detail": "Inserted 4 documents and 3 retention rules"})
