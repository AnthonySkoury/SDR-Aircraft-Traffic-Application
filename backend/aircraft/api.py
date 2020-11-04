from aircraft.models import Aircraft, DataRecord
from rest_framework import viewsets, permissions
from .serializers import AircraftSerializer, DataRecordSerializer, AircraftDataSerializer

# objects.filter(etc) put in what you want 

class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class DataRecordViewSet(viewsets.ModelViewSet):
    queryset = DataRecord.objects.all()
    serializer_class = DataRecordSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class AircraftDataViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.prefetch_related('datarecord_set').all()
    serializer_class = AircraftDataSerializer
    permission_classes = [
        permissions.AllowAny
    ]