from django.forms import ModelForm
from .models import Trip

class TripForm(ModelForm):
  class Meta:
    model = Trip
    fields = ['title', 'start', 'end', 'highlight', 'roadtrip', 'purpose']
