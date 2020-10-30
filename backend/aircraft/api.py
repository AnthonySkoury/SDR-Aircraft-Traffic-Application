from aircraft.models import Aircraft, DataRecord
from rest_framework import viewsets, permissions
from .serializers import AircraftSerializer, DataRecordSerializer, AircraftDataSerializer

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
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    permission_classes = [
        permissions.AllowAny
    ]