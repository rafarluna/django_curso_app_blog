from rest_framework import generics
from ..models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


class EventsAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [IsAuthenticated]


class EventAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [IsAuthenticated]


class EventAttendanceAPIView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    @property
    def pk(self):
        return self.kwargs.get('pk')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(event=self.pk)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['event'] = self.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)