from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()
    datetime = models.DateTimeField()
    place = models.TextField()
    owner = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


TYPE_ATTENDANCE = (('in', 'Interested'),
    ('co', 'confirmed' ))

class Attendance(models.Model):
    event = models.ForeignKey(Event, related_name='attendances', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='attendances', on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPE_ATTENDANCE)

    def __str__(self):
        return self.event.name + ' ' + self.user.full_name
