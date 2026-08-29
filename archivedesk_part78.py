# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: ArchiveDesk
class Document:
    def __init__(self, name, content, tags=None):
        self.name = name
        self.content = content
        self.tags = tags or []
        self.created = datetime.now()

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def get_tag_count(self):
        return len(self.tags)

    def __str__(self):
        return f"Document(name='{self.name}', tags={self.tags})"
