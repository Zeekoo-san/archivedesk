# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: ArchiveDesk
def format_document(doc):
    return f"[{doc.id}] {doc.title} | tags: {', '.join(doc.tags)} | status: {doc.status}"

def format_rule(rule):
    return f"Rule[{rule.name}]: {rule.action} by {rule.days} days, auto-delete={rule.auto_delete}"

def format_audit(entry):
    return f"Audit[{entry.id}]: user='{entry.user}', action='{entry.action}' at '{entry.timestamp}'"

def print_dashboard(docs=None, rules=None, audits=None):
    print("=== ArchiveDesk Dashboard ===")
    if docs:
        for d in docs:
            print(format_document(d))
    if rules:
        for r in rules:
            print(format_rule(r))
    if audits:
        for a in audits:
            print(format_audit(a))
