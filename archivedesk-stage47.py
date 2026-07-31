# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: ArchiveDesk
def demo_scenario():
    import archive_desk as ad

    desk = ad.ArchiveDesk("demo")

    # 1) Create documents with tags
    doc_a = ad.Document("memo_2024", "Meeting notes", ["finance", "internal"])
    doc_b = ad.Document("contract_v3", "Vendor contract revised", ["legal", "external", "confidential"])

    desk.add_document(doc_a)
    desk.add_document(doc_b)

    # 2) Tag documents with additional tags
    desk.tag_document("memo_2024", "approved")
    desk.tag_document("contract_v3", "active")

    # 3) Create retention rules and apply them
    rule_short = ad.RetentionRule("short_term", 90, "delete")
    rule_long = ad.RetentionRule("long_term", 2555, "archive")

    desk.add_retention_rule(rule_short)
    desk.add_retention_rule(rule_long)

    # Set effective dates so rules apply to the documents
    import datetime
    now = datetime.datetime.now()
    doc_a.created_date = now - datetime.timedelta(days=100)
    doc_b.created_date = now - datetime.timedelta(days=30)

    desk.evaluate_retention(now)

    # 4) Search for documents by tag
    results = desk.search_by_tag("legal")
    print(f"Legal documents: {results}")

    # 5) Audit history
    audit = desk.get_audit_log()
    print(f"Audit entries so far: {len(audit)}")

    # 6) Export summary
    print(desk.export_summary())


demo_scenario()
