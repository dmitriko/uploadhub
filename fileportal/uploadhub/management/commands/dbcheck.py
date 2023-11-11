# dbcheck.py
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Checks database availability'

    def handle(self, *args, **options):
        try:
            db_conn = connections['default']
            db_conn.cursor()
        except OperationalError:
            self.stdout.write('Database unavailable, waiting 1 second...')
            return
        else:
            self.stdout.write(self.style.SUCCESS('Database is available'))
