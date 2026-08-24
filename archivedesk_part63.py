# === Stage 63: Add relationships between records where useful ===
# Project: ArchiveDesk
# Step 63: Relationships between records
class Relationship:
    def __init__(self, source_id, target_id, rel_type="references", notes=""):
        self.source_id = source_id
        self.target_id = target_id
        self.rel_type = rel_type
        self.notes = notes

    def to_dict(self):
        return {
            "source_id": self.source_id,
            "target_id": self.target_id,
            "rel_type": self.rel_type,
            "notes": self.notes,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["source_id"], data["target_id"], data["rel_type"], data.get("notes", ""))


class RelationshipManager:
    def __init__(self, records):
        self.records = records
        self._rel_map = {}  # source_id -> list of Relationship

    def add_relationship(self, source_id, target_id, rel_type="references", notes=""):
        rel = Relationship(source_id, target_id, rel_type, notes)
        if source_id not in self._rel_map:
            self._rel_map[source_id] = []
        self._rel_map[source_id].append(rel)

    def get_relationships(self, record_id):
        return self._rel_map.get(record_id, [])

    def get_linked_records(self, record_id):
        rels = self.get_relationships(record_id)
        return [rel.target_id for rel in rels]

    def get_all_relationships(self):
        return [rel.to_dict() for rels in self._rel_map.values() for rel in rels]

    def remove_relationship(self, source_id, target_id):
        if source_id in self._rel_map:
            self._rel_map[source_id] = [
                rel for rel in self._rel_map[source_id]
                if not (rel.source_id == source_id and rel.target_id == target_id)
            ]
            if not self._rel_map[source_id]:
                del self._rel_map[source_id]
