from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Checks database availability'

    def handle(self, *args, **options):
        db_conn = None
        try:
            db_conn = connections['default']
            db_conn.cursor()
        except OperationalError:
            self.stdout.write('Database unavailable, waiting 1 second...')
            return 1  # Return a non-zero exit code to indicate failure
        else:
            self.stdout.write(self.style.SUCCESS('Database is available'))
            return 0  # Return zero to indicate success
