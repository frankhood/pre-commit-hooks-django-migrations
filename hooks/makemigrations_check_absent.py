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
        sys.stdout.write("####################")
        sys.stdout.write(f"output: {output}")
        sys.stdout.write("####################")
    except Exception as ex:
        sys.stdout.write("####################")
        sys.stdout.write(f"eccezione {str(ex)}")
        sys.stdout.write("####################")
        output = ex.output
        sys.stdout.write("####################")
        sys.stdout.write(f"eccezione ex.output {output}")
        sys.stdout.write("####################")
    return output.decode().split("\n")


def main() -> int:
    absent_migrations = False
    for filename in get_absent_migrations():
        sys.stdout.write("####################")
        sys.stdout.write(f"filename {filename}")
        sys.stdout.write("####################")
        if re.match(r".*/migrations/.*\.py", filename.strip()):
            sys.stdout.write("####################")
            sys.stdout.write(f're.match {re.match(r".*/migrations/.*\.py", filename.strip())}')
            sys.stdout.write("####################")
            if not (
                re.match(r".*/root/src/.*\.py", filename)
                or re.match(r".*/.virtualenvs/.*\.py", filename)
                or re.match(r".*/venv/.*\.py", filename)
                or re.match(r".*/site-packages/.*\.py", filename)
            ):
                absent_migrations = True
                sys.stdout.write("####################")
                sys.stdout.write("break")
                sys.stdout.write("####################")
                break
            sys.stdout.write("####################")
            sys.stdout.write("absent_migrations {absent_migrations}")
            sys.stdout.write("####################")
    if absent_migrations:
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
