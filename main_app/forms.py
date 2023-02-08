from django.forms import ModelForm
from .models import Visit
from django import forms

class VisitForm(ModelForm):
  class Meta:
    model = Visit
    fields = '__all__'
