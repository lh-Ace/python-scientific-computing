"""Repository bootstrap checks—not a substitute for student assessment.

We use the standard library's `unittest` for the initial scaffold so the
first lesson does not depend on pytest or NumPy. Students do not need to
understand test internals in Lesson 01.01.
"""

import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LESSON_FILE = REPO_ROOT / "lessons/01-python-foundations/01-01-running-python/hello.py"


class BootstrapChecks(unittest.TestCase):
    def test_first_program_can_run(self):
        result = subprocess.run(
            [sys.executable, str(LESSON_FILE)],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("Scientific Python: my first program", result.stdout)
        self.assertIn("5", result.stdout.splitlines())


if __name__ == "__main__":
    unittest.main()
