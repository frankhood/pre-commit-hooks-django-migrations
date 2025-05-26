import re
import subprocess
import sys

MAKEMIGRATIONS_CHECK_CMD = [
    "python",
    "manage.py",
    "makemigrations",
    "--check",
    "--dry-run",
]


def get_absent_migrations():
    try:
        output = subprocess.check_output(MAKEMIGRATIONS_CHECK_CMD)
        sys.stderr.write("####################")
        sys.stderr.write(f"output: {output}")
        sys.stderr.write("####################")
    except Exception as ex:
        sys.stderr.write("####################")
        sys.stderr.write(f"eccezione {str(ex)}")
        sys.stderr.write("####################")
        output = ex.output
        sys.stderr.write("####################")
        sys.stderr.write(f"eccezione ex.output {output}")
        sys.stderr.write("####################")
    return output.decode().split("\n")


def main() -> int:
    absent_migrations = False
    for filename in get_absent_migrations():
        sys.stderr.write("####################")
        sys.stderr.write(f"filename {filename}")
        sys.stderr.write("####################")
        if re.match(r".*/migrations/.*\.py", filename.strip()):
            sys.stderr.write("####################")
            sys.stderr.write(f"re.match {re.match(r".*/migrations/.*\.py", filename.strip())}")
            sys.stderr.write("####################")
            if not (
                re.match(r".*/root/src/.*\.py", filename)
                or re.match(r".*/.virtualenvs/.*\.py", filename)
                or re.match(r".*/venv/.*\.py", filename)
                or re.match(r".*/site-packages/.*\.py", filename)
            ):
                absent_migrations = True
                sys.stderr.write("####################")
                sys.stderr.write("break")
                sys.stderr.write("####################")
                break
            sys.stderr.write("####################")
            sys.stderr.write("absent_migrations {absent_migrations}")
            sys.stderr.write("####################")
    if absent_migrations:
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
