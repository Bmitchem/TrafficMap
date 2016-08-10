from rest_framework import serializers

from injestor.models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Trip