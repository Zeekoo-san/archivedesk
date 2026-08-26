# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: ArchiveDesk
def generate_changelog():
    """Generate a compact changelog from the audit log.

    Reads the audit log and returns a formatted changelog string
    summarizing the most recent activities.
    """
    if not os.path.exists(AUDIT_LOG):
        return "No audit log found."

    with open(AUDIT_LOG, 'r') as f:
        lines = f.readlines()

    changelog = []
    for line in lines[-50:]:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) >= 3:
            date = parts[0].strip()
            action = parts[1].strip()
            detail = parts[2].strip()
            changelog.append(f"{date} | {action} | {detail}")

    return '\n'.join(changelog) if changelog else "No recent activities."
