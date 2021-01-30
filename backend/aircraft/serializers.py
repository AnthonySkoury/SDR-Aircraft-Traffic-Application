from rest_framework import serializers
from aircraft.models import Aircraft, DataRecord, UserNotification

# Serializers are used to convert the SQL data into JSON or JSON into SQL

# Serializer for aircraft with default model operations
class AircraftSerializer(serializers.ModelSerializer):

    # Define base model and fields to be displayed
    class Meta:
        model = Aircraft
        fields = '__all__'

# Serializer for data records with default model operations
class DataRecordSerializer(serializers.ModelSerializer):

    # Define base model and fields to be displayed
    class Meta:
        model = DataRecord
        fields = '__all__'

# Serializer for aircraft data joined with data records for list operation
class AircraftDataSerializer(serializers.ModelSerializer):
    # Serialize data records with the one to many relation
    datarecord_set = DataRecordSerializer(many=True)

    # Define base model and fields to be displayed
    class Meta:
        model = Aircraft
        fields = '__all__'

class UserNotificationSerializer(serializers.ModelSerializer):

    # Define base model and fields to be displayed
    class Meta:
        model = UserNotification
        fields = '__all__'