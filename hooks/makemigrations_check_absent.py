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
        result = subprocess.run(
            MAKEMIGRATIONS_CHECK_CMD,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            text=True  # per avere stringa direttamente, da Python 3.7+
        )
        output = result.stdout
    except Exception as ex:
        output = str(ex)  # fallback
    return output.split("\n")

def main() -> int:
    absent_migrations = False
    for filename in get_absent_migrations():
        if re.match(r".*/migrations/.*\.py", filename.strip()):
            if not (
                re.match(r".*/root/src/.*\.py", filename)
                or re.match(r".*/.virtualenvs/.*\.py", filename)
                or re.match(r".*/venv/.*\.py", filename)
                or re.match(r".*/site-packages/.*\.py", filename)
            ):
                absent_migrations = True
                break
    if absent_migrations:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
