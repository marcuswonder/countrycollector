from django.db import models
from django.urls import reverse

PURPOSE = (
    ('L', 'Leisure'),
    ('B', 'Business'),
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

class Visit(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    purpose = models.CharField(
        max_length=1,
        choices=PURPOSE,
        default=PURPOSE[0][0]
    )
    highlight = models.TextField(max_length=250)
    road_trip = models.BooleanField(default=False)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_purpose_display} visit starting on {self.start_date}"