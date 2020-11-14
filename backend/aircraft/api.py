from aircraft.models import Aircraft, DataRecord
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .serializers import AircraftSerializer, DataRecordSerializer, AircraftDataSerializer
from django.db.models import Prefetch

# Viewsets are used as the interface between the users with the data models/tables

# Aircraft viewset with CRUD operation defaults from ModelViewSet
class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()

    # Serialize SQL into JSON or JSON into SQL
    serializer_class = AircraftSerializer
    
    permission_classes = [
        permissions.AllowAny
    ]

# Data Record viewset with CRUD operation defaults from ModelViewSet
class DataRecordViewSet(viewsets.ModelViewSet):
    queryset = DataRecord.objects.all()

    # Serialize SQL into JSON or JSON into SQL
    serializer_class = DataRecordSerializer

    permission_classes = [
        permissions.AllowAny
    ]

# Aircraft Data joined with Data Record Viewset with only list operation allowed
class AircraftDataViewSet(viewsets.ViewSet):
    # queryset = Aircraft.objects.prefetch_related(Prefetch('datarecord_set', queryset=DataRecord.objects.order_by('-timestamp'))).all()
    serializer_class = AircraftDataSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    # Query parameters defined here
    # Get aircraft joined with data
    def list(self, request):
        data_query=DataRecord.objects.all()

        # Query param for getting records for an exact ICAO
        icaos = self.request.GET.get('icao', None)
        if icaos:
            data_query = data_query.filter(icao=icaos)
        
        # Query param for getting records for an exact timestamp
        exact_date = self.request.GET.get('exact-date', None)
        if exact_date:
            data_query = data_query.filter(timestamp=exact_date)

        # Order data by descending timestamps by default
        data_query = data_query.order_by('-timestamp')

        # Join the two datarecord tables with the aircraft table via foreign key
        queryset = Aircraft.objects.prefetch_related(Prefetch('datarecord_set', queryset=data_query)).all()

        # Serialize the SQL data into JSON
        serializer = AircraftDataSerializer(queryset, many=True)

        # Send response
        return Response(serializer.data)

