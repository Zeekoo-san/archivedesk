# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: ArchiveDesk
import unittest
from datetime import date, timedelta
from archive_desk.models.retention_rule import RetentionRule
from archive_desk.validators.retain_validator import RetainValidator


class TestRetentionRule(unittest.TestCase):
    def test_rule_creation(self):
        rule = RetentionRule(
            name="Annual Reports",
            tag="reports",
            retention_days=365,
            disposition="archive"
        )
        self.assertEqual(rule.name, "Annual Reports")
        self.assertEqual(rule.tag, "reports")
        self.assertEqual(rule.retention_days, 365)

    def test_rule_creation_invalid_disposition(self):
        with self.assertRaises(ValueError):
            RetentionRule(name="Test", tag="test", retention_days=10, disposition="invalid")


class TestRetainValidator(unittest.TestCase):
    def setUp(self):
        self.validator = RetainValidator()

    def test_valid_retained_document(self):
        doc = {"tag": "reports", "created_date": (date.today() - timedelta(days=400)).isoformat()}
        result = self.validator.validate(doc, ["Annual Reports"])
        self.assertTrue(result["retained"])

    def test_invalid_expired_document(self):
        doc = {"tag": "reports", "created_date": (date.today() - timedelta(days=500)).isoformat()}
        result = self.validator.validate(doc, ["Annual Reports"])
        self.assertFalse(result["retained"])


if __name__ == "__main__":
    unittest.main()
