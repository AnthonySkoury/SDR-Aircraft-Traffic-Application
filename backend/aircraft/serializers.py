from rest_framework import serializers
from aircraft.models import Aircraft, DataRecord

class AircraftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aircraft
        fields = '__all__'

class DataRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataRecord
        fields = '__all__'

class AircraftDataSerializer(serializers.ModelSerializer):
    datarecords = DataRecordSerializer(many=True)
    class Meta:
        model = Aircraft
        fields = ['icao', 'name', 'aircraft_type', 'datarecords']