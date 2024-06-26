from django.shortcuts import render
from rest_framework import viewsets
from .models import lecture
from .serializers import LectureSerializers

# Create your views here.

class LectureView(viewsets.ModelViewSet):
    queryset = lecture.objects.all()
    serializer_class = LectureSerializers
    name = "Lecture API"
    description = "API for managing lecture"