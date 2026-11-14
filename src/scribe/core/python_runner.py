from pathlib import Path
import subprocess
import sys


class PythonRunner:
    """Runs Python scripts."""

    def pythonrun(
        self, path: str | Path
    ) -> subprocess.CompletedProcess[str]:
        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(
                f"Python file not found: {path}"
            )

        if path.suffix != ".py":
            raise ValueError(
                "Scribe currently supports only Python files."
            )

        return subprocess.run(
            [sys.executable, str(path)],
            capture_output=True,
            text=True,
        )