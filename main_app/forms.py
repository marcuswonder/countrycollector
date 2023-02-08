from django.forms import ModelForm
from .models import Visit

class VisitForm(ModelForm):
  class Meta:
    model = Visit
    fields = ['title', 'start', 'end', 'highlight', 'roadtrip', 'purpose']
