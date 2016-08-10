from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Trip(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    pickup_lat = models.DecimalField(decimal_places=12, max_digits=15, db_index=True)
    pickup_long = models.DecimalField(decimal_places=12, max_digits=15, db_index=True)
    dropoff_lat = models.DecimalField(decimal_places=12, max_digits=15, db_index=True)
    dropoff_long = models.DecimalField(decimal_places=12, max_digits=15, db_index=True)
    base = models.CharField(max_length=6)

    def get_duration(self):
        return self.end - self.start

    def __unicode__(self):
        return "Trip from (%s) to (%s)" % (self.start, self.end)