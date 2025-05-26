

import re
import sys
from django.core.management.base import BaseCommand

from pre_commit_absent_migrations.makemigrations_check_absent import get_absent_migrations


class Command(BaseCommand):
    def handle(self, *args, **options):
        absent_migrations = []
        for filename in get_absent_migrations():
            if re.match(r".*/migrations/.*\.py", filename.strip()):
                if not (
                    re.match(r".*/root/src/.*\.py", filename)
                    or re.match(r".*/.virtualenvs/.*\.py", filename)
                    or re.match(r".*/venv/.*\.py", filename)
                    or re.match(r".*/site-packages/.*\.py", filename)
                ):
                    absent_migrations.append(filename)
        if absent_migrations:
            self.stderr.write(f"❌ Migrazioni necessarie:")
            for absent_migration in absent_migrations:
                self.stderr.write(f"- {absent_migration}")
            sys.exit(1)
        

        
