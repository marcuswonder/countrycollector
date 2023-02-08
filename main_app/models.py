from django.db import models
from django.urls import reverse
from django import forms

PURPOSES = (
    ('L', 'Leisure'),
    ('B', 'Business')
)

ROADTRIP = (
    ('Y', 'Yes'),
    ('N', 'No')
)

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    capital_city = models.CharField(max_length=100)
    population = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'country_id': self.id})
    
    class Meta:
        verbose_name_plural = "countries"


class Visit(models.Model):
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

    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-start']
