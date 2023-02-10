from django.forms import ModelForm
from .models import Segment

class SegmentForm(ModelForm):
  class Meta:
    model = Segment
    fields = ['segment_type', 'start_date', 'end_date', 'segment_country_start', 'start_location', 'journey_type', 'distance_measurement', 'distance', 'duration_hrs', 'stay_type', 'stay_name', 'stay_location', 'stay_map', 'activity_type', 'activity_description', 'organiser_type', 'organiser_name', 'organiser_email', 'organiser_telephone']

    
