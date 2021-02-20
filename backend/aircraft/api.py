from aircraft.models import Aircraft, DataRecord, UserNotification
from rest_framework import viewsets, permissions, status, renderers
from rest_framework.response import Response
# from rest_framework.decorators import action

from .serializers import AircraftSerializer, DataRecordSerializer, AircraftDataSerializer, UserNotificationSerializer
from django.db.models import Prefetch, Q
import boto3 # for AWS SNS
import os
from django.conf import settings
from decimal import Decimal
# from django.http import FileResponse

# Viewsets are used as the interface between the users with the data models/tables

# Feature flag for AWS SMS notification system
notif_enabled = False

# get keys for AWS
f = open(os.path.join(settings.BASE_DIR, 'backend_keys.txt'))
enable = f.readline().rstrip('\n')
if enable.lower() in ['true', '1', 't', 'y', 'yes']:
    notif_enabled = True

if notif_enabled:
    key_id = f.readline().rstrip('\n')
    access_key = f.readline().rstrip('\n')

    # Create an SNS client
    client = boto3.client(
        "sns",
        aws_access_key_id=key_id,
        aws_secret_access_key=access_key,
        region_name="us-west-2"
    )


def send_sms(number, msg):
    # Send sms message
    client.publish(
        PhoneNumber=number,
        Message=msg
    )

def check_notif(long, lat):

    res = UserNotification.objects.filter(Q(latitude1__lte=lat, longitude1__lte=long, latitude2__gte=lat, longitude2__gte=long) | Q(latitude1__gte=lat, longitude1__gte=long, latitude2__lte=lat, longitude2__lte=long))
    if len(res) != 0:
        print("Notifying users")
        for notif in res:
            number = str(notif.phone)
            long1 = str(notif.longitude1)
            lat1 = str(notif.latitude1)
            long2 = str(notif.longitude2)
            lat2 = str(notif.latitude2)
            msg = "An aircraft was detected in the region bound lat1,long1 ("+lat1+","+long1+") and lat2,long2 ("+lat2+","+long2+")."
            send_sms(number, msg)


def get_query(request):
    data_query=DataRecord.objects.all()

    # Query param for getting records for an exact ICAO
    icaos = request.GET.get('icao', None)
    if icaos:
        data_query = data_query.filter(icao=icaos)

    # Query param for getting records for an exact timestamp
    exact_date = request.GET.get('exact-date', None)
    if exact_date:
        data_query = data_query.filter(timestamp=exact_date)

    # Query param for getting records in a range of timestamps
    start_time = request.GET.get('start-time', None)
    end_time = request.GET.get('end-time', None)
    if start_time and end_time:
        data_query = data_query.filter(timestamp__range=(start_time, end_time))

    # Query param for getting records in a long and lat range
    x1 = request.GET.get('lat1', None)
    y1 = request.GET.get('long1', None)
    x2 = request.GET.get('lat1', None)
    y2 = request.GET.get('long2', None)
    if x1 and y1 and x2 and y2:
        data_query = data_query.filter(latitude__range=(x1, x2), longitude__range=(y1, y2))

    return data_query

class PassthroughRenderer(renderers.BaseRenderer):
    """
        Return data as-is. View should supply a Response.
    """
    media_type = ''
    format = ''
    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data

# Aircraft viewset with CRUD operation defaults from ModelViewSet
class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()

    # Serialize SQL into JSON or JSON into SQL
    serializer_class = AircraftSerializer

    permission_classes = [
        permissions.AllowAny
    ]

    # Override Create method to allow serialization of many or single objects when inserting
    def create(self, request, pk=None, company_pk=None, project_pk=None):
        # Check if the request data is a list or a single object
        is_many = isinstance(request.data, list)
        
        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        # Insert data after serializing
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # Return response
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# Data Record viewset with CRUD operation defaults from ModelViewSet
class DataRecordViewSet(viewsets.ModelViewSet):
    queryset = DataRecord.objects.all()

    # Serialize SQL into JSON or JSON into SQL
    serializer_class = DataRecordSerializer

    permission_classes = [
        permissions.AllowAny
    ]

    # Override Create method to allow serialization of many or single objects when inserting
    def create(self, request, pk=None, company_pk=None, project_pk=None):
        # Check if the request data is a list or a single object
        is_many = isinstance(request.data, list)

        if not is_many and notif_enabled:
            print(type(request), request)
            print(type(request.data), request.data)
            check_notif(Decimal(request.data['longitude']), Decimal(request.data['latitude']))
        
        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        # Insert data after serializing
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # Return response
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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
        data_query = get_query(self.request)

        # Order data by descending timestamps by default
        data_query = data_query.order_by('-timestamp')

        # Join the two datarecord tables with the aircraft table via foreign key
        queryset = Aircraft.objects.prefetch_related(Prefetch('datarecord_set', queryset=data_query)).all()

        # Serialize the SQL data into JSON
        serializer = AircraftDataSerializer(queryset, many=True)

        # Send response
        return Response(serializer.data)

# User Notification viewset with CRUD operation defaults from ModelViewSet
class UserNotificationViewSet(viewsets.ModelViewSet):
    queryset = UserNotification.objects.all()

    # Serialize SQL into JSON or JSON into SQL
    serializer_class = UserNotificationSerializer

    permission_classes = [
        permissions.AllowAny
    ]

# class DownloadDBViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Aircraft.objects.prefetch_related(Prefetch('datarecord_set', queryset=DataRecord.objects.order_by('-timestamp'))).all()
#     serializer_class = AircraftSerializer

#     @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
#     def download(self, *args, **kwargs):
#         instance = self.get_object()

#         # get an open file handle (I'm just using a file attached to the model for this example):
#         file_handle = instance.file.open()

#         # send file
#         response = FileResponse(file_handle, content_type='whatever')
#         response['Content-Length'] = instance.file.size
#         response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name

#         return response
