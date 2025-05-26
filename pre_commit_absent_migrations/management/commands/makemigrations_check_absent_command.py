

import re
from django.core.management.base import BaseCommand

from pre_commit_absent_migrations.makemigrations_check_absent import get_absent_migrations


class Command(BaseCommand):
    def handle(self, *args, **options):
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

        
