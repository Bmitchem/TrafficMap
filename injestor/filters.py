import django_filters
from injestor.models import Trip
from rest_framework import filters

class TripFilter(filters.BaseFilterBackend):
    # min lookups
    min_lat = django_filters.NumberFilter()
    min_long = django_filters.NumberFilter()
    
    # max lookups
    max_lat = django_filters.NumberFilter()
    max_long = django_filters.NumberFilter()