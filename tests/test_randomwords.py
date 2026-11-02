# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

spec = importlib.util.spec_from_file_location("randomwords", Path(__file__).resolve().parents[1] / "randwords.py")
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)

class RandomWordsTests(unittest.TestCase):
    def test_unique_words(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "words.txt"
            path.write_text("chat\nchien\nchat\nlapin\noiseau\n", encoding="utf-8")
            result = app.choose_words(path, 3)
            self.assertEqual(len(result), 3)
            self.assertEqual(len(set(result)), 3)
            self.assertTrue(set(result) <= {"chat", "chien", "lapin", "oiseau"})
    def test_rejects_bad_counts(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "words.txt"
            path.write_text("chat\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                app.choose_words(path, 2)
            with self.assertRaises(ValueError):
                app.choose_words(path, 0)

if __name__ == "__main__":
    unittest.main()
