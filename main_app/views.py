from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Country, Trip, Segment
import requests
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
 


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def countries_index(request):
  countries = Country.objects.all()
  return render(request, 'countries/index.html', { 'countries': countries })

def trips_index(request):
  trips = Trip.objects.all()
  return render(request, 'trips/index.html', { 'trips': trips })

def segments_index(request):
  segments = Segment.objects.all()
  return render(request, 'segments/index.html', { 'segments': segments })

def countries_detail(request, country_id):
  country = Country.objects.get(id=country_id)
  return render(request, 'countries/detail.html', { 
    'country': country,
  })

def trips_detail(request, trip_id):
  trip = Trip.objects.get(id=trip_id)
  countries = Country.objects.all()
  segments = Segment.objects.all()
  return render(request, 'trips/detail.html', { 
    'trip': trip,
    'countries': countries,
    'segments': segments
  })

def segments_detail(request, segment_id):
  segment = Segment.objects.get(id=segment_id)
  return render(request, 'segments/detail.html', { 
    'segment': segment,
  })

class CountryCreate(CreateView):
  model = Country
  fields = '__all__'

class TripCreate(CreateView):
  model = Trip
  fields = ['title', 'start', 'end', 'highlight', 'roadtrip', 'purpose']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
  # success_url = '/trips'

class SegmentCreate(CreateView):
  model = Segment
  fields = '__all__'

class CountryUpdate(UpdateView):
  model = Country
  fields = '__all__'

class TripUpdate(UpdateView):
  model = Trip
  fields = '__all__'

class SegmentUpdate(UpdateView):
  model = Segment
  fields = '__all__'

class CountryDelete(DeleteView):
  model = Country
  success_url = '/countries'

class TripDelete(DeleteView):
  model = Trip
  success_url = '/trips'

class SegmentDelete(DeleteView):
  model = Segment
  success_url = '/segments'

def assoc_country(request, trip_id, country_id):
    Trip.objects.get(id=trip_id).countries.add(country_id)
    return redirect('detail', trip_id=trip_id)

def assoc_segment(request, trip_id, segment_id):
    Trip.objects.get(id=trip_id).segments.add(segment_id)
    return redirect('detail', trip_id=trip_id)

def fetchCountries(request):
  try:
    response = requests.get("https://restcountries.com/v3.1/all").json()
    for r in response:
      if r['name']['common'] == "Antarctica":
        pass
      else:
        country = Country(
          name=r['name']['common'],
          continent=r['region'],
          population=r['population']
        )
        country.save()
  except Exception as e:
    print("An error occurred while fetching countries: ", e)
  return response


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)