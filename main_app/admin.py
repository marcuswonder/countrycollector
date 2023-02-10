from django.contrib import admin
from .models import Country, Trip, Segment

# Register your models here.
admin.site.register(Country)
admin.site.register(Trip)
admin.site.register(Segment)