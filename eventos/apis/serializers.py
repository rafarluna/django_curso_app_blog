from rest_framework import serializers
from ..models import *

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'datetime', 'place']