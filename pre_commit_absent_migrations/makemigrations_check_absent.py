import click
import re
import subprocess
from . import settings


MAKEMIGRATIONS_CHECK_CMD = [
    "python",
    "manage.py",
    "makemigrations",
    "--check",
    "--dry-run",
]


def get_absent_migrations():
    try:
        output = subprocess.check_output(
            MAKEMIGRATIONS_CHECK_CMD, stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as ex:
        output = ex.output
    return output.decode().split("\n")


def main() -> int:
    absent_migrations = []
    fail = 0
    for filename in get_absent_migrations():
        if re.match(r".*/migrations/.*\.py", filename.strip()):
            if not (
                re.match(r".*/root/src/.*\.py", filename)
                or re.match(r".*/.virtualenvs/.*\.py", filename)
                or re.match(r".*/venv/.*\.py", filename)
                or re.match(r".*/site-packages/.*\.py", filename)
            ):
                fail = 1
                absent_migrations.append(filename)
                break
    if fail:
        print(
            f"❌ {settings.CRED}[ERROR] Some migrations are missing!\nAbsent migrations: {settings.CEND}"
        )
        for migration in absent_migrations:
            print(f"- {migration}\n")

    return fail


@click.command()
def makemigrations_check_absent():
    exit(main())


if __name__ == "__main__":
    exit(main())
