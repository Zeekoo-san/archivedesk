# === Stage 19: Add undo support for the last simple mutation ===
# Project: ArchiveDesk
def undo():
    if not _undo_stack:
        print("Nothing to undo.")
        return None
    action = _undo_stack.pop()
    action.undo()
    print(f"Undo applied: {action.description}")
    return action
