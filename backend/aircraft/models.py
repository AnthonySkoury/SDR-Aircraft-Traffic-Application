from django.db import models

# Database Tables defined in Django Models

# Aircraft data model
class Aircraft(models.Model):
    # Data fields
    icao = models.CharField(primary_key=True, max_length=6)
    callsign = models.CharField(blank=True, max_length=7)
    squawk = models.CharField(blank=True, max_length=4)
    name = models.CharField(blank=True, max_length=30)
    aircraft_type = models.CharField(blank=True, max_length=30)

    class Meta:
        # Table name in Postgresql
        db_table = 'aircraft_table'

# Data Record model
class DataRecord(models.Model):
    # Data fields
    data_record_id = models.AutoField(primary_key=True, editable=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    icao = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    ground_speed = models.DecimalField(max_digits=20, decimal_places=5)
    altitude = models.DecimalField(max_digits=20, decimal_places=5)
    
    class Meta:
        # Table name in Postgresql
        db_table = 'data_record_table'
        # Ensure there can't be a duplicate ICAO and timestamp combination
        unique_together = (('timestamp','icao'),)