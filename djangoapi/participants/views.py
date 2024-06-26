from django.shortcuts import render
from rest_framework import viewsets
from .models import Participant
from .serializers import ParticipantSerializers

# Create your views here.

class ParticipantView(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializers
    name = "Participant API"
    description = "API for managing participants"