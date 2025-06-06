from click.testing import CliRunner
from pre_commit_absent_migrations import makemigrations_check_absent
from pre_commit_absent_migrations.makemigrations_check_absent import (
    makemigrations_check_absent as check_absent_function,
)


# =======================================================================================
# pytest tests/test_check_absent.py
# =======================================================================================


def test_cli_runs(monkeypatch):
    monkeypatch.setattr(
        makemigrations_check_absent.subprocess,
        "check_output",
        lambda *args, **kwargs: b"",
    )
    runner = CliRunner()
    result = runner.invoke(check_absent_function)

    assert result.exception is None


def test_main_no_migrations(monkeypatch):
    monkeypatch.setattr(
        makemigrations_check_absent.subprocess,
        "check_output",
        lambda *args, **kwargs: b"",
    )
    assert makemigrations_check_absent.main() == 0


def test_main_with_migrations(monkeypatch):
    output = b"/project/app/migrations/0001_initial.py\n"
    monkeypatch.setattr(
        makemigrations_check_absent.subprocess,
        "check_output",
        lambda *args, **kwargs: output,
    )
    assert makemigrations_check_absent.main() == 1
