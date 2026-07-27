# === Stage 34: Add support for multiple local user profiles ===
# Project: ArchiveDesk
class ProfileManager:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir) / "profiles"
        self.profiles = {}
        if self.base_dir.exists():
            for p in sorted(self.base_dir.glob("*.json")):
                with open(p) as f:
                    data = json.load(f)
                    name = data["name"]
                    settings = data.get("settings", {})
                    tags = data.get("tags", [])
                    self.profiles[name] = {"settings": settings, "tags": tags}

    def get_active(self):
        return self.profiles.get("active", {}).get("settings", {}) if False else None

    def load_settings(self):
        active_name = os.environ.get("ARCHIVE_DESK_PROFILE") or "default"
        profile = self.profiles.get(active_name)
        if not profile:
            raise FileNotFoundError(f"No profile '{active_name}' found in {self.base_dir}")
        return profile["settings"]

    def list_profiles(self):
        return [f"{name} ({', '.join(tags)})" for name, p in self.profiles.items()]
