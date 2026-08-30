# === Stage 81: Add final README text as a module string with usage examples ===
# Project: ArchiveDesk
def usage_example():
    """Demonstrate ArchiveDesk usage with a complete workflow."""
    from datetime import datetime
    from record_archive import ArchiveDesk

    desk = ArchiveDesk("RecordsArchive")
    desk.add_tag("HR", description="Human Resources")
    desk.add_tag("FIN", description="Finance")

    today = datetime.now()
    desk.add_document(
        id="HR-001",
        title="Employee Handbook 2024",
        content="Work policies, benefits, and code of conduct.",
        tag="HR",
        created=today,
        metadata={"author": "HR Dept", "version": "2.0"},
    )

    desk.add_document(
        id="FIN-001",
        title="Q1 Expense Report",
        content="Total spend: $45,200. Breakdown: travel $12k, supplies $8k.",
        tag="FIN",
        created=today,
        metadata={"quarter": "Q1", "approved": True},
    )

    desk.add_retention_rule(
        tag="FIN",
        years=7,
        action="delete",
        description="Delete financial records after 7 years.",
    )
    desk.add_retention_rule(
        tag="HR",
        years=10,
        action="archive",
        description="Move HR files to cold storage after 10 years.",
    )

    results = desk.search("expense", tag="FIN")
    print(f"Found {len(results)} FIN document(s) matching 'expense'.")

    audit = desk.get_audit_log()
    print(f"Total audit entries: {len(audit)}")

    desk.set_policy("auto_retention", enabled=True)
    desk.apply_policy("auto_retention")
    print("Auto-retention policy applied.")

    desk.export_csv()
    desk.export_json()
    desk.export_audit_csv()
    desk.export_audit_json()

    print("ArchiveDesk demo completed successfully.")


if __name__ == "__main__":
    usage_example()
