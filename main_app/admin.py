from django.contrib import admin
from .models import Country, Trip, City

# Register your models here.
admin.site.register(Country)
admin.site.register(Trip)
admin.site.register(City)