from rest_framework import serializers
from ..models import *
from rest_framework.exceptions  import NotAcceptable


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'datetime', 'place']


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'event', 'user', 'type']

    def validate(self, data):
        if Attendance.objects.filter(event=data['event'], user=data['user']).exists():
            raise serializers.ValidationError("usuario ya registrado")
        return data
