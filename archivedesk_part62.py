# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: ArchiveDesk
def prioritize_documents(documents, rules, search_query=None):
    scored = []
    for doc in documents:
        score = 0
        if doc.get("retention_status") in ("expired", "overdue"):
            score += 10
        if doc.get("is_encrypted"):
            score += 5
        if search_query:
            if search_query.lower() in doc.get("title", "").lower():
                score += 3
            if search_query.lower() in doc.get("content", "").lower():
                score += 2
        if doc.get("tags"):
            for tag in doc["tags"]:
                if tag.lower() in ("critical", "urgent", "legal"):
                    score += 4
                elif tag.lower() in ("routine", "low_priority"):
                    score -= 2
        scored.append((score, doc))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [doc for _, doc in scored]
