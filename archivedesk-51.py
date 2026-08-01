# === Stage 51: Add unit tests for search and filter behavior ===
# Project: ArchiveDesk
import unittest
from archive_desk.models import Document, Tag
from archive_desk.search import search_documents_by_query


class TestSearchAndFilter(unittest.TestCase):
    def setUp(self):
        self.doc1 = Document(id=1, title="Q1 Report", content="quarterly data 2024")
        self.doc2 = Document(id=2, title="Budget Plan", content="annual budget forecast")
        self.doc3 = Document(id=3, title="Meeting Notes", content="team sync discussion")

    def test_search_matches_keywords(self):
        results = search_documents_by_query("quarterly data 2024")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, 1)

    def test_search_no_match(self):
        results = search_documents_by_query("xyz unknown")
        self.assertEqual(len(results), 0)

    def test_case_insensitive(self):
        results = search_documents_by_query("QUARTERLY DATA")
        self.assertEqual(len(results), 1)

    def test_partial_title_match(self):
        results = search_documents_by_query("budget")
        self.assertTrue(any(d.title == "Budget Plan" for d in results))


if __name__ == "__main__":
    unittest.main()
