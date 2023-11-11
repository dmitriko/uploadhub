from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Checks database availability'

    def handle(self, *args, **kwargs):
        db_conn = None
        try:
            db_conn = connections['default']
            c = db_conn.cursor()
        except OperationalError:
            self.stdout.write('Database unavailable, waiting 1 second...')
            return 1  # Non-zero exit code to signal failure
        else:
            self.stdout.write(self.style.SUCCESS('Database is available'))
            c.close()
            return 0
