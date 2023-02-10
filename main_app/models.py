from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

PURPOSES = (
    ('L', 'Leisure'),
    ('B', 'Business')
)

ROADTRIP = (
    ('Y', 'Yes'),
    ('N', 'No')
)

SEGMENT_TYPE = (
    ('J', 'Journey'),
    ('S', 'Stay'),
    ('A', 'Activity')
)

JOURNEY_TYPE = (
    ('A', 'By Air'),
    ('S', 'By Sea'),
    ('D', 'By Road'),
    ('L', 'By Rail'),
    ('O', 'Other')
)

DISTANCE_MEASUREMENT = (
    ('M', 'miles'),
    ('K', 'kilometres')
)

STAY_TYPE = (
    ('H', 'Hotel'),
    ('G', 'Guesthouse'),
    ('C', 'Campsite'),
    ('W', 'Wild Camping'),
    ('O', 'Other')
)

ACTIVITY_TYPE = (
    ('A', 'Active'),
    ('V', 'Adventurous'),
    ('C', 'Cultural'),
    ('S', 'Shopping'),
    ('E', 'Sightseeing'),
    ('H', 'Historical'),
    ('O', 'Other')
)

ORGANISER_TYPE = (
    ('S', 'Self-Organised'),
    ('T', 'Tour Operator'),
    ('G', 'Guide')
)

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    population = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('country_detail', kwargs={'country_id': self.id})
    
    class Meta:
        verbose_name_plural = "countries"


class Trip(models.Model):
    title = models.CharField(max_length=100)
    start = models.DateField('Start Date')
    end = models.DateField('End Date')
    highlight = models.TextField(max_length=250)
    roadtrip = models.CharField(
        max_length=1,
        choices=ROADTRIP,
        default=ROADTRIP[1][0]
    )
    purpose = models.CharField(        
        max_length=1,
        choices=PURPOSES,
        default=PURPOSES[0][0]
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} on {self.start}"

    def get_absolute_url(self):
        return reverse('trip_detail', kwargs={'trip_id': self.id})

    class Meta:
        ordering = ['-start']


class Segment(models.Model):
    segment_type = models.CharField(
        choices=SEGMENT_TYPE,
        max_length=1,
    )
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')

    segment_country_start = models.ManyToManyField(
        Country,
        max_length=100,
    )
    
    # ------------ Journey ------------

    start_location = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    journey_type = models.CharField(
        choices=JOURNEY_TYPE,
        max_length=1,
        blank=True,
        null=True
    )

    distance_measurement = models.CharField(
        choices=DISTANCE_MEASUREMENT,
        max_length=1,
        blank=True,
        null=True
    )

    distance = models.IntegerField(
        blank=True,
        null=True
    )

    duration_hrs = models.IntegerField(
        blank=True,
        null=True
    )

    # ------------ Stay ------------

    stay_type = models.CharField(
        choices=STAY_TYPE,
        max_length=1,
        blank=True,
        null=True
    )
   
    stay_name = models.CharField(
        max_length=100,
        help_text="The name of the hotel, campsite, guesthouse or a description of your wild camping",
        blank=True,
        null=True
    )

    stay_location = models.CharField(
        max_length=100,
        help_text="Save the longitude and latitude to help yourself and others find your stay again!",
        blank=True,
        null=True
    )

    stay_map = models.CharField(
        max_length=300,
        help_text="Save a map link to help yourself and others find your stay again!",
        blank=True,
        null=True
    )
    
    # ------------ Activity ------------

    activity_type = models.CharField(
        choices=ACTIVITY_TYPE,
        max_length=1,
        blank=True,
        null=True
    )

    activity_description = models.TextField(
        max_length=300,
        blank=True,
        null=True
    )

    organiser_type = models.CharField(
        choices=ORGANISER_TYPE,
        max_length=1,
        blank=True,
        null=True
    )

    organiser_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    organiser_email = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    organiser_telephone = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.segment_type} on {self.start_date}"
    

    def get_absolute_url(self):
        return reverse('segment_detail', kwargs={'segment_id': self.id})





