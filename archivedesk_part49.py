# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: ArchiveDesk
import unittest
from collections import OrderedDict


class RecordsArchiveDeskTest(unittest.TestCase):
    """Unit tests for update and delete edge cases."""

    def setUp(self):
        self.desk = RecordsArchiveDesk()

    # ── Update edge cases ──────────────────────────────────────

    def test_update_preserves_id_and_tags_on_same_record(self):
        rec1 = {"id": "R001", "content": "hello", "tags": ["intro"]}
        self.desk.store_records([rec1])
        updated = {"id": "R001", "content": "world", "tags": ["intro"]}
        result = self.desk.update_record(updated)
        self.assertEqual(result["id"], "R001")
        self.assertIn("update", self.desk.audit_log[-1])

    def test_update_changes_tags(self):
        rec1 = {"id": "R002", "content": "x", "tags": ["a"]}
        self.desk.store_records([rec1])
        updated = {"id": "R002", "content": "x", "tags": ["b"]}
        result = self.desk.update_record(updated)
        self.assertEqual(result["tags"], ["b"])

    def test_update_with_nonexistent_id_returns_none(self):
        rec1 = {"id": "FAKE", "content": "nope", "tags": []}
        result = self.desk.update_record(rec1)
        self.assertIsNone(result)

    # ── Delete edge cases ──────────────────────────────────────

    def test_delete_existing_record(self):
        rec1 = {"id": "R003", "content": "bye", "tags": []}
        self.desk.store_records([rec1])
        deleted = self.desk.delete_record("R003")
        self.assertTrue(deleted)

    def test_delete_nonexistent_record(self):
        rec1 = {"id": "NOPE", "content": "x", "tags": []}
        self.desk.store_records([rec1])
        deleted = self.desk.delete_record("NOPE")
        self.assertFalse(deleted)

    # ── Combined behaviour ─────────────────────────────────────

    def test_search_after_update_and_delete(self):
        recs = [
            {"id": "A", "content": "keep",  "tags": ["x"]},
            {"id": "B", "content": "remove","tags": []},
        ]
        self.desk.store_records(recs)
        result = self.desk.update_record({"id": "A", "content": "updated", "tags": ["y"]})
        self.assertEqual(result["content"], "updated")
        self.assertTrue(self.desk.delete_record("B"))
        found = self.desk.search("keep")
        self.assertFalse(found)
