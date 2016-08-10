from django.contrib import admin

# Register your models here.
from injestor.models import Trip

class TripAdmin(admin.ModelAdmin):
    list_display = ('start', 'pickup_lat', 'pickup_long', 'end', 'dropoff_lat', 'dropoff_long')

admin.site.register(Trip, admin.ModelAdmin)