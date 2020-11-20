from rest_framework import routers
from .api import AircraftViewSet, DataRecordViewSet, AircraftDataViewSet, DownloadDBViewSet

# Define URLs for API

router = routers.DefaultRouter()
router.register('api/aircraft', AircraftViewSet, 'aircraft')
router.register('api/datarecord', DataRecordViewSet, 'datarecord')
router.register('api/aircraftdata', AircraftDataViewSet, 'aircraftdata')
router.register('api/downloaddb', DownloadDBViewSet, 'downloaddb')

urlpatterns = router.urls