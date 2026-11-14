from pathlib import Path
from scribe.core.python_runner import PythonRunner


def test_run_python_file():
    runner = PythonRunner()
    script_path  = (
        Path(__file__).parent
        / "fixtures"
        / "hello.py"
    )
    result = runner.pythonrun(script_path)
    assert result.returncode == 0
    assert result.stdout == "Hello world, name is Scribe\n"
    assert result.stderr == ""
