import sys

from scribe.core.runner import PythonRunner

def main()->None:
    if len(sys.argv)<3:
        print("Usage: scribe run <file.py>")
        return
    command = sys.argv[1]
    path = sys.argv[2]

    if command == "run":
        runner = PythonRunner()
        result = runner.pythonrun(path)
        if result.stdout:
            print(result.stdout,end="")
        if result.stderr:
            print(result.stderr,file=sys.stderr,end="")
        raise SystemExit(result.returncode)
    print(f"Unknown command:{command}")

if __name__ == '__main__':
    main()
        
