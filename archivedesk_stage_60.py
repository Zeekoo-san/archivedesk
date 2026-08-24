# === Stage 60: Add saved views for frequently used filters ===
# Project: ArchiveDesk
import json
from pathlib import Path

class SavedView:
    def __init__(self, name, filters=None, sort=None, limit=None):
        self.name = name
        self.filters = filters or {}
        self.sort = sort or {"field": "date", "direction": "desc"}
        self.limit = limit

    def to_dict(self):
        return {"name": self.name, "filters": self.filters, "sort": self.sort, "limit": self.limit}

    @classmethod
    def from_dict(cls, d):
        return cls(name=d["name"], filters=d.get("filters", {}), sort=d.get("sort", {}), limit=d.get("limit"))


class SavedViewManager:
    def __init__(self, archive_db):
        self.archive_db = archive_db
        self.views_path = Path("archive_desk/saved_views.json")

    def save_view(self, view):
        if not isinstance(view, SavedView):
            raise ValueError("View must be a SavedView instance")
        views = self._load_views()
        views.append(view.to_dict())
        self._save_views(views)
        self.archive_db.log_audit("saved_view", view.name)
        return view

    def load_view(self, name):
        views = self._load_views()
        for v in views:
            if v["name"] == name:
                return SavedView.from_dict(v)
        return None

    def delete_view(self, name):
        views = self._load_views()
        filtered = [v for v in views if v["name"] != name]
        if len(filtered) == len(views):
            raise ValueError(f"Saved view '{name}' not found")
        self._save_views(filtered)
        self.archive_db.log_audit("deleted_view", name)
        return True

    def list_views(self):
        return self._load_views()

    def _load_views(self):
        if self.views_path.exists():
            return json.loads(self.views_path.read_text())
        return []

    def _save_views(self, views):
        self.views_path.write_text(json.dumps(views, indent=2))
