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
        sys.stderr.write("output", output)
    except Exception as ex:
        sys.stderr.write("eccezione", str(ex))
        output = ex.output
        sys.stderr.write("eccezione ex.output", output)
    return output.decode().split("\n")


def main() -> int:
    absent_migrations = False
    for filename in get_absent_migrations():
        sys.stderr.write("filename", filename)
        if re.match(r".*/migrations/.*\.py", filename.strip()):
            sys.stderr.write("re.match", re.match(r".*/migrations/.*\.py", filename.strip()))
            if not (
                re.match(r".*/root/src/.*\.py", filename)
                or re.match(r".*/.virtualenvs/.*\.py", filename)
                or re.match(r".*/venv/.*\.py", filename)
                or re.match(r".*/site-packages/.*\.py", filename)
            ):
                absent_migrations = True
                sys.stderr.write("break")
                break
            sys.stderr.write("absent_migrations", absent_migrations)
    if absent_migrations:
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
