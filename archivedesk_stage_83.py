# === Stage 83: Add regression tests for the final demo workflow ===
# Project: ArchiveDesk
import sys
sys.path.insert(0, "/mnt/data")

def demo_workflow():
    from archivedesk import ArchiveDesk, Document, Tag, RetentionRule, AuditEntry

    desk = ArchiveDesk("demo_archive")

    # Step 1: Create documents
    doc1 = Document("Contract_2023", content="Annual service agreement", tags=[Tag("contract"), Tag("2023")])
    doc2 = Document("Invoice_001", content="Payment receipt for Q1", tags=[Tag("invoice"), Tag("Q1")])
    doc3 = Document("Memo_42", content="Internal team memo", tags=[Tag("memo")])

    # Step 2: Define retention rules
    rule1 = RetentionRule("perpetual", label="Perpetual", retention_period=999999, description="Keep forever")
    rule2 = RetentionRule("7_year", label="7 Year", retention_period=7, description="7-year financial retention")

    # Step 3: Apply rules to documents
    doc1.retention_rule = rule1
    doc2.retention_rule = rule2
    doc3.retention_rule = rule1

    # Step 4: Search for documents
    results = desk.search("contract")
    assert len(results) == 1
    assert results[0].title == "Contract_2023"

    # Step 5: Verify audit trail
    audit_entries = desk.get_audit_history()
    assert len(audit_entries) >= 3
    assert any(entry.action == "document_created" for entry in audit_entries)

    # Step 6: Verify retention status
    assert doc1.retention_status == "perpetual"
    assert doc2.retention_status == "pending_review"

    print("All demo workflow tests passed successfully!")
    return True

demo_workflow()
