# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: ArchiveDesk
def dry_run(self, command: str) -> dict:
    """Simulate a mutating command without actually changing state."""
    self._validate(command)
    action = _ACTION_MAP.get(command, None)
    if action is None:
        return {"status": "dry-run", "message": f"Unknown command '{command}' (not supported for dry-run)", "affected_records": 0}

    result = {
        "status": "dry-run",
        "command": command,
        "expected_outcome": action.get("description", ""),
        "affected_records": 0,
        "warnings": [],
    }

    if command == "archive" or command == "delete":
        result["warnings"].append(f"'{command}' would permanently {action['description']}. Confirm before enabling real execution.")

    return result
