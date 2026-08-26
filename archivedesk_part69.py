# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: ArchiveDesk
def reset_demo_data(db):
    """Clear all tables and re-insert demo records for quick testing."""
    db.exec("DELETE FROM audit_log")
    db.exec("DELETE FROM retention_rule")
    db.exec("DELETE FROM tag")
    db.exec("DELETE FROM document")
    db.exec("DELETE FROM user")

    db.exec("INSERT INTO user (id, username, password_hash, role) VALUES ('u1', 'admin', 'admin123', 'admin')")
    db.exec("INSERT INTO user (id, username, password_hash, role) VALUES ('u2', 'viewer', 'viewer123', 'viewer')")

    db.exec("INSERT INTO tag (id, name) VALUES ('t1', 'invoice')")
    db.exec("INSERT INTO tag (id, name) VALUES ('t2', 'contract')")

    db.exec("INSERT INTO retention_rule (id, tag_id, years, status) VALUES ('r1', 't1', 7, 'active')")
    db.exec("INSERT INTO retention_rule (id, tag_id, years, status) VALUES ('r2', 't2', 20, 'active')")

    db.exec("INSERT INTO document (id, title, content, owner_id, created_at, updated_at) VALUES ('d1', 'Sample Invoice', 'Invoice #1001, Amount: $500', 'u1', '2023-01-15', '2023-01-15')")
    db.exec("INSERT INTO document (id, title, content, owner_id, created_at, updated_at) VALUES ('d2', 'Sample Contract', 'Contract #C001, Parties: A and B', 'u1', '2023-02-20', '2023-02-20')")

    db.exec("INSERT INTO audit_log (id, user_id, action, document_id, timestamp) VALUES ('a1', 'u1', 'create', 'd1', '2023-01-15 10:00:00')")
    db.exec("INSERT INTO audit_log (id, user_id, action, document_id, timestamp) VALUES ('a2', 'u2', 'read', 'd1', '2023-03-10 14:30:00')")

    print("Demo data reset complete.")
