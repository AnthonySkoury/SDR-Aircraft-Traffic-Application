from aircraft.models import Aircraft, DataRecord
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .serializers import AircraftSerializer, DataRecordSerializer, AircraftDataSerializer
from django.db.models import Prefetch


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

class AircraftDataViewSet(viewsets.ViewSet):
    # queryset = Aircraft.objects.prefetch_related(Prefetch('datarecord_set', queryset=DataRecord.objects.order_by('-timestamp'))).all()
    serializer_class = AircraftDataSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    # Get aircraft joined with data
    def list(self, request):
        data_query=DataRecord.objects.all()

        icaos = self.request.GET.get('icao', None)
        if icaos:
            data_query = data_query.filter(icao=icaos)
        
        exact_date = self.request.GET.get('exact-date', None)
        if exact_date:
            data_query = data_query.filter(timestamp=exact_date)

        data_query = data_query.order_by('-timestamp')

        queryset = Aircraft.objects.prefetch_related(Prefetch('datarecord_set', queryset=data_query)).all()

        serializer = AircraftDataSerializer(queryset, many=True)

        return Response(serializer.data)

