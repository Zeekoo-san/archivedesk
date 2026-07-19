# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: ArchiveDesk
def search_documents(self, query: str) -> List[Document]:
    """Case-insensitive search across document content and metadata."""
    results = []
    for doc in self.documents.values():
        if not isinstance(doc, dict):
            continue
        searchable = {
            'content': getattr(doc, 'content', ''),
            'title': getattr(doc, 'title', ''),
            'author': getattr(doc, 'author', ''),
            'date': str(getattr(doc, 'date', '')),
            'status': getattr(doc, 'status', ''),
        }
        query_lower = query.lower()
        if any(query_lower in field for field in searchable.values()):
            results.append(doc)
    return results
