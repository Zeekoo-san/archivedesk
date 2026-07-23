# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: ArchiveDesk
def tag_add_remove(documents, tag_name):
    """Add all documents to a tag and remove them if they were already tagged."""
    for doc in documents:
        tags = set(doc.get('tags', []))
        if tag_name not in tags:
            tags.add(tag_name)
            doc['tags'] = sorted(tags)

def tag_summary(documents, tag_name):
    """Return a dict of count and list of document ids for the given tag."""
    matched = [d for d in documents if tag_name in (set(d.get('tags', [])))]
    return {'tag': tag_name, 'count': len(matched), 'ids': [d['id'] for d in matched]}
