from rest_framework import generics
from ..models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.exceptions  import NotAcceptable
from .permissions import EventPermission


class EventsAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [IsAuthenticated, EventPermission]

    #def create(self, request, *args, **kwargs):
        # '''cuando creo un evento el owner debo ser yo mismo'''        
        # data = request.data.copy()
        # data['event'] = self.pk
        # print('soy quien dice ser', request.data['owner'], request.user.id)
        #if request.data['owner'] != request.user.id:
        #    raise NotAcceptable('Solo puedes crear tus propios eventos')
        #serializer = self.get_serializer(data=request.data)
        #serializer.is_valid(raise_exception=True)
        #self.perform_create(serializer)
        #headers = self.get_success_headers(serializer.data)
        #return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class EventAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [IsAuthenticated, EventPermission]

    # solo el propietario del evento puede modificarlo


class EventAttendancesAPIView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendancesSerializer
    permission_classes = [IsAuthenticated]

    @property
    def pk(self):
        return self.kwargs.get('pk')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(event=self.pk)

    def create(self, request, *args, **kwargs):
        # solo puedo crear mi propia asistencia

        data = request.data.copy()
        data['event'] = self.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class EventAttendanceAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    @property
    def event_pk(self):
        return self.kwargs.get('event_pk')

    @property
    def pk(self):
        return self.kwargs.get('pk')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(event=self.event_pk, id=self.pk)

    # solo puedo modificar y eliminar mi propia asistencia
