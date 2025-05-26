

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from pre_commit_absent_migrations import makemigrations_check_absent
        makemigrations_check_absent()
        
