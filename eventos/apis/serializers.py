from rest_framework import serializers
from ..models import *

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'datetime', 'place', 'owner']

    # def validate_owner(self, value):
    #     request = self.context['request']
    #     if value != request.user.id:
    #         raise serializers.ValidationError("Solo puedes crear tus propios eventos")
    #     return value
        

class AttendancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'event', 'user', 'type']

    def validate(self, data):
        if Attendance.objects.filter(event=data['event'], user=data['user']).exists():
            raise serializers.ValidationError("usuario ya registrado")
        return data


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'event', 'user', 'type']
