from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.
from .models import Lead
from .serializers import AircraftSerializer
from rest_framework import generics

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = AircraftSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('icao','data_record_set__timestamp')

    def get_queryset(self):
        queryset = Lead.objects.all().order_by('-id')[:10]
        return reversed(queryset)

    def get(self, request):
        queryset = self.get_query()
        serializer = AircraftSerializer(queryset)
        return Response(serializer.data)
