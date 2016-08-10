"""
Management command to import the UBER data,

splits the dataset in half and applies half of the data for pickup locations and the other half for
dropoff locations. checks to make sure users don't arrive before they left and if so swaps the dropoff/pickup stats

Prints out helpful progress data while importing.

Args:
    filepath (str): relative path to the data_set file
"""
import csv
import os

import datetime
import time
import sys
from django.apps import apps
from django.core.management import BaseCommand
from django.db import transaction

class Command(BaseCommand):
    help = 'Injests an Uber trip csv file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    @transaction.atomic()
    def handle(self, *args, **options):
        Trip = apps.get_model('injestor.Trip')
        file_path = options['file_path']
        assert os.path.exists(file_path), 'Error: Could not find file path \"%s\", are you sure it exists?' % file_path
        trips = []
        with open(file_path, 'r') as fp:
            data = csv.DictReader(fp)
            rows = [row for row in data]
        start_time = time.time()
        for i, row in enumerate(rows[::2]):
            pickup, dropoff = row, rows[i+1]

            str_format = '%m/%d/%Y %H:%M:%S'

            clean_pickup_date = datetime.datetime.strptime(pickup['Date/Time'], str_format)
            clean_dropoff_date = datetime.datetime.strptime(dropoff['Date/Time'], str_format)

            # You can't get picked up after you arrive
            if pickup['Date/Time'] > dropoff["Date/Time"]:
                pickup, dropoff = dropoff, pickup
                clean_pickup_date, clean_dropoff_date = clean_dropoff_date, clean_pickup_date

            trips.append(Trip(start=clean_pickup_date,
                              end=clean_dropoff_date,
                              pickup_lat=pickup['Lat'],
                              pickup_long=pickup['Lon'],
                              dropoff_lat=dropoff['Lat'],
                              dropoff_long=dropoff['Lon'],
                              base=pickup['Base']))
            if i % 10000 == 0:
                current_time = time.time()
                sys.stdout.write('\rProcessed %s, elapsed time: %s' % (i, current_time-start_time))
                sys.stdout.flush()

        sys.stdout.write('\nWriting Objects')
        Trip.objects.bulk_create(trips)
        sys.stdout.write('\nImport finished, total time %s' % (time.time() - start_time))









if __name__ == "__main__":
    import django
    django.setup()
    c = Command()
    c.handle(file_path='/Users/bmitchem/PersonalPycharmProjects/UBERATCapp/uber-trip-data/uber-raw-data-apr14.csv')