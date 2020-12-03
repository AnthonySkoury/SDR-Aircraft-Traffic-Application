from django.db import models

# Database Tables defined in Django Models

# Fields added inspired from Dump1090 broadcasted fields as well as ADS-B Exchange

# Aircraft is split from Data Record to avoid data redundancy

# Aircraft data model
class Aircraft(models.Model):

    # Options for fields

    # Species options
    Species_None = 0
    Species_Land_Plane = 1
    Species_Sea_Plane = 2
    Species_Amphibian = 3
    Species_Helicopter = 4
    Species_Gyrocopter = 5
    Species_Tiltwing = 6
    Species_Ground_Vehicle = 7
    Species_Tower = 8

    species_choices = [
        (Species_None, 'None'),
        (Species_Land_Plane, 'Land Plane'),
        (Species_Sea_Plane, 'Sea Plane'),
        (Species_Amphibian, 'Amphibian'),
        (Species_Helicopter, 'Helicopter'),
        (Species_Gyrocopter, 'Gyrocopter'),
        (Species_Tiltwing, 'Species Tiltwing'),
        (Species_Ground_Vehicle, 'Ground Vehicle'),
        (Species_Tower, 'Tower')
    ]

    # Engine Type options
    Engine_Type_None = 0
    Engine_Type_Piston = 1
    Engine_Type_Turboprop = 2
    Engine_Type_Jet = 3
    Engine_Type_Electric = 4

    engine_type_choices = [
        (Engine_Type_None, 'None'),
        (Engine_Type_Piston, 'Piston'),
        (Engine_Type_Turboprop, 'Turboprop'),
        (Engine_Type_Jet, 'Jet'),
        (Engine_Type_Electric, 'Electric')
    ]

    # Engine Mount options
    Engine_Mount_Unknown = 0
    Engine_Type_Aft_Mounted = 1
    Engine_Type_Wing_Buried = 2
    Engine_Type_Fuselage_Buried = 3
    Engine_Type_Nose_Mounted = 4
    Engine_Type_Wing_Mounted = 5

    engine_mount_choices = [
        (Engine_Type_Aft_Mounted, 'Unknown'),
        (Engine_Type_Aft_Mounted, 'Aft Mounted'),
        (Engine_Type_Wing_Buried, 'Wing Buried'),
        (Engine_Type_Fuselage_Buried, 'Fuselage Buried'),
        (Engine_Type_Nose_Mounted, 'Nose Mounted'),
        (Engine_Type_Wing_Mounted, 'Wing Mounted')
    ]

    # Data fields

    # Six digit hexadecimal unique aircraft identifier
    icao = models.CharField(primary_key=True, max_length=6)
    # Aircraft callsign
    callsign = models.CharField(blank=True, max_length=7)
    # Aircraft squawk transponder code
    squawk = models.CharField(blank=True, max_length=4)

    # Fields not broadcasted and can be looked up via the web (user can send update request later)

    # Airline name or private owner 
    name = models.CharField(blank=True, max_length=30)
    # The aircraft model’s ICAO type code
    aircraft_type = models.CharField(blank=True, max_length=30)
    # Aircraft registration number
    registration_number = models.CharField(blank=True, max_length=30)
    # A description of the aircraft’s model
    aircraft_model = models.CharField(blank=True, max_length=100)
    # Aircraft manufacturer's name
    aircraft_manufacturer = models.CharField(blank=True, max_length=50)
    # Year an aircraft was manufactuered
    aircraft_year = models.CharField(blank=True, max_length=4)
    # The aircraft’s construction or serial number
    construction_number = models.CharField(blank=True, max_length=30)
    # The name of the aircraft's operator
    aircraft_operator = models.CharField(blank=True, max_length=30)
    # General Aircraft Type
    aircraft_species = models.CharField(blank=True, choices=species_choices, max_length=30)
    # Type of engine the aircraft uses
    engine_type = models.CharField(blank=True, choices=engine_type_choices, max_length=30)
    # The placement of engines on the aircraft
    engine_mount = models.CharField(blank=True, choices=engine_mount_choices, max_length=30)

    class Meta:
        # Table name in Postgresql
        db_table = 'aircraft_table'

# Data Record model
class DataRecord(models.Model):
    # Data fields

    # Data Record identifier that auto increments
    data_record_id = models.AutoField(primary_key=True, editable=False)
    # Timestamp for when Dump1090 data was uploaded in SDR script
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    # Six digit hexadecimal unique aircraft identifier
    icao = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    # Aircraft's longitude above ground
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # Aircraft's latitude above ground
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    # Boolean that is True if the received aircraft position is valid
    valid_position = models.BooleanField(blank=True)
    # Aircraft ground speed in knots
    ground_speed = models.DecimalField(max_digits=20, decimal_places=5)
    # Altitude in feet at standard pressure
    altitude = models.DecimalField(max_digits=20, decimal_places=5)

    # Vertical speed in feet per minute
    vertical_rate = models.DecimalField(blank=True, max_digits=20, decimal_places=5)
    # Aircraft’s track angle across the ground clockwise from 0° north.
    track = models.DecimalField(blank=True, max_digits=10, decimal_places=5)
    # Boolean that is True if the received aircraft track is valid
    valid_track = models.BooleanField(blank=True)
    # The number of seconds that the aircraft has been tracked for.  Will change as aircraft roams between receiving servers.
    tracked_seconds = models.CharField(blank=True, max_length=30)
    # The count of messages received for the aircraft.  Will change as aircraft roams between receiving servers.
    count_messages = models.CharField(blank=True, max_length=30)

    
    class Meta:
        # Table name in Postgresql
        db_table = 'data_record_table'
        # Ensure there can't be a duplicate ICAO and timestamp combination
        unique_together = (('timestamp','icao'),)