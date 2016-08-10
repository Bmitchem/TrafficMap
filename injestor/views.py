import datetime
from django.shortcuts import render

# Create your views here.
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.filters import DjangoFilterBackend
from rest_framework.response import Response

from injestor.filters import TripFilter
from injestor.serializers import TripSerializer

from injestor.models import Trip


class TripViewSet(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()

    def filter_queryset(self, queryset):
        min_lat = self.request.query_params.get('min_lat')
        min_long = self.request.query_params.get('min_long')

        max_lat = self.request.query_params.get('max_lat')
        max_long = self.request.query_params.get('max_long')

        start_date = self.request.query_params.get('start')
        end_date = self.request.query_params.get('end')

        if min_lat:
            self.queryset = self.queryset.filter(dropoff_lat__gte=min_lat, pickup_lat__gte=min_lat)

        if min_long:
            self.queryset = self.queryset.filter(dropoff_long__gte=min_long, pickup_long__gte=min_long)

        if max_lat:
            self.queryset = self.queryset.filter(dropoff_lat__lte=max_lat, pickup_lat__lte=max_lat)

        if max_long:
            self.queryset = self.queryset.filter(dropoff_long__lte=max_long, pickup_long__lte=max_long)

        if start_date:
            start_date = datetime.datetime.strptime(start_date, "%m/%d/%Y %I:%M %p")
            self.queryset = self.queryset.filter(start__gte=start_date)

        if end_date:
            end_date = datetime.datetime.strptime(end_date, "%m/%d/%Y %I:%M %p")
            self.queryset = self.queryset.filter(end__lte=end_date)

        return self.queryset



