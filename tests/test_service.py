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


if __name__ == "__main__":
    unittest.main()