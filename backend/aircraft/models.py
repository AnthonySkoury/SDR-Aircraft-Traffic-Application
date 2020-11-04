from django.db import models

# # Create your models here.
class Aircraft(models.Model):
    icao = models.CharField(primary_key=True, max_length=6)
    callsign = models.CharField(blank=True, max_length=6)
    name = models.CharField(blank=True, max_length=30)
    aircraft_type = models.CharField(blank=True, max_length=30)
    class Meta:
        db_table = 'aircraft_table'

class DataRecord(models.Model):
    timestamp = models.DateTimeField(primary_key=True, auto_now=False, auto_now_add=False)
    icao = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    ground_speed = models.DecimalField(max_digits=20, decimal_places=5)
    altitude = models.DecimalField(max_digits=20, decimal_places=5)
    
    class Meta:
        db_table = 'data_record_table'
        unique_together = (('timestamp','icao'),)