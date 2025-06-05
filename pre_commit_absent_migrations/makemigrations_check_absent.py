import click
import re
import subprocess

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


@click.command()
def makemigrations_check_absent():
    exit(main())


if __name__ == "__main__":
    exit(main())
