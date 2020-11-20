from django.shortcuts import render

# Create your views here.
from .models import Lead
from .serializers import AircraftSerializer
from rest_framework import generics

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = AircraftSerializer
