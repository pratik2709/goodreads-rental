import datetime

from django.contrib.auth.models import User
from django.core.management import BaseCommand

from rent_engine.models import Customer, CategoryInformation, BooksCatalogue, BooksRented


class Command(BaseCommand):
    help = 'loads data in the database'

    def handle(self, *args, **options):
        # management.call_command('flush', interactive=False)
        util = DataLoadingCleaningUtils()
        util.add_data()


class DataLoadingCleaningUtils:

    def __init__(self):
        pass

    def add_data(self):
        user, created = User.objects.get_or_create(username="prat")
        user.set_password('123')
        user.save()
