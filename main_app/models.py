from django.db import models
from django.urls import reverse

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