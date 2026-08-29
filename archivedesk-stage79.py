# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: ArchiveDesk
import os
from datetime import datetime
from typing import List, Dict

def run_self_check() -> Dict[str, object]:
    """Self-check: validate file structure, demo operations, and report results."""
    results: Dict[str, object] = {"status": "ok", "checks": [], "errors": []}

    # Check 1: Verify required files exist
    required_files = [
        "archive_desk.py",
        "requirements.txt",
        "README.md",
        "LICENSE",
        "docs/ARCHITECTURE.md",
        "docs/INSTALL.md",
        "docs/DESIGN.md",
        "docs/TESTING.md",
        "docs/CONTRIBUTING.md",
        "docs/CHANGELOG.md",
    ]

    for f in required_files:
        if not os.path.exists(f):
            results["status"] = "error"
            results["errors"].append(f"Missing required file: {f}")
            continue
        results["checks"].append(f"{f}: exists")

    # Check 2: Import and instantiate ArchiveDesk
    try:
        from archive_desk import ArchiveDesk
        desk = ArchiveDesk()
        results["checks"].append("ArchiveDesk: instantiated")
    except Exception as e:
        results["status"] = "error"
        results["errors"].append(f"Failed to instantiate ArchiveDesk: {e}")

    # Check 3: Demo - add documents with tags and retention
    if desk:
        desk.add_document("doc1", "2024-01-15", "Tax Return 2023", "financial", "retained", 7)
        desk.add_document("doc2", "2024-02-20", "Employee Handbook", "hr", "retained", 5)
        desk.add_document("doc3", "2024-03-10", "Expired Invoice", "finance", "expired", 3)
        desk.add_document("doc4", "2024-04-05", "Project Plan", "project", "archived", 10)
        results["checks"].append("Demo: added 4 documents")

    # Check 4: Demo - add tags
    if desk:
        desk.add_tag("compliance")
        desk.add_tag("audit")
        desk.add_tag("high_priority")
        results["checks"].append("Demo: added 3 tags")

    # Check 5: Demo - add retention rules
    if desk:
        desk.add_retention_rule("financial_records", 7, "retained")
        desk.add_retention_rule("hr_documents", 5, "retained")
        desk.add_retention_rule("project_docs", 10, "archived")
        results["checks"].append("Demo: added 3 retention rules")

    # Check 6: Demo - search
    if desk:
        search_result = desk.search("financial")
        results["checks"].append(f"Demo: search returned {len(search_result)} results")

    # Check 7: Demo - apply retention rules
    if desk:
        desk.apply_retention_rules()
        results["checks"].append("Demo: applied retention rules")

    # Check 8: Demo - audit log
    if desk:
        audit_log = desk.get_audit_log()
        results["checks"].append(f"Demo: audit log has {len(audit_log)} entries")

    # Check 9: Verify audit log contents
    if desk:
        if len(audit_log) > 0:
            results["checks"].append("Audit log: populated correctly")
        else:
            results["errors"].append("Audit log: empty after operations")

    # Check 10: Verify documents are retained correctly
    if desk:
        retained_docs = desk.get_documents_by_status("retained")
        if len(retained_docs) > 0:
            results["checks"].append(f"Retention: {len(retained_docs)} documents retained")
        else:
            results["errors"].append("Retention: no documents retained")

    # Final status
    if results["errors"]:
        results["status"] = "failed"

    return results
