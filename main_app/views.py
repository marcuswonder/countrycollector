from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Country, Trip, City
 


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

def countries_detail(request, country_id):
  country = Country.objects.get(id=country_id)
  return render(request, 'countries/detail.html', { 
    'country': country,
  })

def trips_detail(request, trip_id):
  trip = Trip.objects.get(id=trip_id)
  countries = Country.objects.all()
  cities = City.objects.all()
  return render(request, 'trips/detail.html', { 
    'trip': trip,
    'countries': countries,
    'cities': cities
  })

class CountryCreate(CreateView):
  model = Country
  fields = '__all__'

class TripCreate(CreateView):
  model = Trip
  fields = ['title', 'start', 'end', 'highlight', 'roadtrip', 'purpose', 'countries', 'cities']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
  # success_url = '/trips'

class CityCreate(CreateView):
  model = City
  fields = '__all__'

class CountryUpdate(UpdateView):
  model = Country
  fields = '__all__'

class TripUpdate(UpdateView):
  model = Trip
  fields = '__all__'

class CountryDelete(DeleteView):
  model = Country
  success_url = '/countries'

class TripDelete(DeleteView):
  model = Trip
  success_url = '/trips'

def assoc_country(request, trip_id, country_id):
    Trip.objects.get(id=trip_id).countries.add(country_id)
    return redirect('detail', trip_id=trip_id)

def assoc_city(request, trip_id, city_id):
    Trip.objects.get(id=trip_id).cities.add(city_id)
    return redirect('detail', trip_id=trip_id)