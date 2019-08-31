from django.urls import path
from .views import *

urlpatterns = [
    path('eventos/', EventsAPIView.as_view()),
    path('eventos/<int:pk>/', EventAPIView.as_view())
]
