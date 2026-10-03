import tempfile
import unittest
from pathlib import Path

from devlog.service import DevLogService
from devlog.storage import JsonStorage


class DevLogServiceTest(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

        path = Path(self.temp_dir.name) / "test.json"

        self.service = DevLogService(
            JsonStorage(str(path))
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_entry(self):
        entry = self.service.add_entry(
            "Implement CLI parser",
            ["python", "cli"],
        )

        self.assertEqual(
            entry.message,
            "Implement CLI parser",
        )

        self.assertEqual(
            entry.tags,
            ["python", "cli"],
        )

    def test_list_entries(self):
        self.service.add_entry("First entry")
        self.service.add_entry("Second entry")

        entries = self.service.list_entries()

        self.assertEqual(len(entries), 2)

    def test_delete_entry(self):
        entry = self.service.add_entry(
            "Temporary note"
        )

        result = self.service.delete_entry(
            entry.id
        )

        self.assertTrue(result)
        self.assertEqual(
            len(self.service.list_entries()),
            0,
        )

    def test_delete_unknown_entry(self):
        result = self.service.delete_entry(
            "unknown"
        )

        self.assertFalse(result)

    def test_search_by_message(self):
        self.service.add_entry(
            "Implement authentication middleware",
            ["backend"],
        )

        self.service.add_entry(
            "Update project documentation",
            ["docs"],
        )

        results = self.service.search_entries(
            query="authentication"
        )

        self.assertEqual(len(results), 1)

        self.assertEqual(
            results[0].message,
            "Implement authentication middleware",
        )

    def test_filter_by_tag(self):
        self.service.add_entry(
            "Fix login redirect",
            ["bug", "backend"],
        )

        self.service.add_entry(
            "Update README",
            ["docs"],
        )

        results = self.service.search_entries(
            tag="backend"
        )

        self.assertEqual(len(results), 1)

    def test_search_with_query_and_tag(self):
        self.service.add_entry(
            "Improve API error handling",
            ["backend", "api"],
        )

        self.service.add_entry(
            "Improve README examples",
            ["docs"],
        )

        results = self.service.search_entries(
            query="improve",
            tag="api",
        )

        self.assertEqual(len(results), 1)

        self.assertEqual(
            results[0].message,
            "Improve API error handling",
        )

if __name__ == "__main__":
    unittest.main()