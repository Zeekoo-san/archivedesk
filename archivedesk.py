# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: ArchiveDesk
import uuid
from datetime import date, timedelta

class Document:
    def __init__(self, title, content, created_by, created_on):
        self.id = str(uuid.uuid4())[:8]
        self.title = title
        self.content = content
        self.author = created_by
        self.created = created_on

class RetentionRule:
    def __init__(self, tag, years, archive_date=None):
        self.tag = tag
        self.years = years
        self.archive_date = archive_date or date.today() - timedelta(days=730)

# Demo data
docs = [
    Document("HR Policy 2021", "Employee handbook text...", "Alice"),
    Document("Q4 Sales Report", "Revenue figures Q4...", "Bob"),
    Document("Meeting Notes Jan", "Key discussion points...", "Carol"),
]
rules = [RetentionRule("confidential", 5), RetentionRule("temporary", 2)]
