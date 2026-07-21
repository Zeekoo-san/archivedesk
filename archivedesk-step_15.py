# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: ArchiveDesk
def dispatch(text):
    text = text.strip().lower()
    if not text:
        return None
    commands = {
        "help": print_help,
        "list docs": list_docs,
        "add doc <name>": add_doc_cmd,
        "tag <doc_id> <tag_name>": tag_doc_cmd,
        "search <query>": search_cmd,
        "retention check": retention_check_cmd,
    }
    for cmd_str, handler in commands.items():
        if text == cmd_str:
            return handler()
    parts = text.split(None, 1)
    if not parts[0]:
        return None
    cmd_key = parts[0].lower().replace(" ", "")
    if cmd_key in ("adddoc", "adddoc"):
        rest = parts[1] if len(parts) > 1 else ""
        name = rest.strip() or "untitled"
        return add_doc_cmd(name)
    if cmd_str.startswith("tag") and text:
        tag_parts = text.split(None, 2)
        if len(tag_parts) >= 3:
            doc_id = tag_parts[1].strip().lower()
            tag_name = tag_parts[2].strip()
            return tag_doc_cmd(doc_id, tag_name)
    return None
