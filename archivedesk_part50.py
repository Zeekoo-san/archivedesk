# === Stage 50: Add unit tests for import and export behavior ===
# Project: ArchiveDesk
import unittest, json, os

class TestImportExport(unittest.TestCase):
    def setUp(self):
        from project import ArchiveDesk
        self.ad = ArchiveDesk()

    def test_import_from_json_file(self):
        path = "archive_desk.json"
        with open(path, "w") as f:
            json.dump({"documents": [{"id": "d1", "title": "Test"}, {"id": "d2", "title": "Another"}],
                        "tags": ["important"], "retention_rules": [], "audit_log": []}, f)
        self.ad.import_from_file(path)
        self.assertEqual(len(self.ad.get_documents()), 2)
        os.remove(path)

    def test_export_to_json_file(self):
        path = "archive_desk.json"
        self.ad.add_document("d1", "Hello")
        self.ad.add_tag("urgent")
        self.ad.export_to_file(path)
        with open(path) as f:
            data = json.load(f)
        self.assertEqual(data["documents"][0]["title"], "Hello")
        self.assertIn("urgent", data["tags"])
        os.remove(path)

if __name__ == "__main__":
    unittest.main()
