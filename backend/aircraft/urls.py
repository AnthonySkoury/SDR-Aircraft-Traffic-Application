from rest_framework import routers
from .api import AircraftViewSet, DataRecordViewSet, AircraftDataViewSet

router = routers.DefaultRouter()
router.register('api/aircraft', AircraftViewSet, 'aircraft')
router.register('api/datarecord', DataRecordViewSet, 'datarecord')
router.register('api/aircraftdata', AircraftDataViewSet, 'aircraftdata')

urlpatterns = router.urls