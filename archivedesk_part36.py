# === Stage 36: Add templates for quickly creating common records ===
# Project: ArchiveDesk
class Template:
    def __init__(self, name, doc_type, fields=None):
        self.name = name
        self.doc_type = doc_type
        self.fields = fields or {}

    def apply(self, data=None):
        if data is None:
            data = {}
        for k, v in self.fields.items():
            data.setdefault(k, v)
        return data


templates_db = []
