from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Country, Trip, City
from .forms import TripForm
 


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
  trip_form = TripForm()
  return render(request, 'countries/detail.html', { 
    'country': country,
    'trip_form': trip_form 
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
  fields = '__all__'

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

def add_trip(request):
  form = TripForm(request.POST)
  print(form.is_valid())
  if form.is_valid():
    new_trip = form.save(commit=False)
    form.instance.user = request.user
    new_trip.save()
    trip_id = new_trip.id
  return redirect('trip_detail', trip_id=trip_id)

def new_trip(request):
  trip_form = TripForm()
  return render(request, 'trips/add.html', { 
    'trip_form': trip_form 
  })

def assoc_country(request, trip_id, country_id):
    Trip.objects.get(id=trip_id).countries.add(country_id)
    return redirect('detail', trip_id=trip_id)

def assoc_city(request, trip_id, city_id):
    Trip.objects.get(id=trip_id).cities.add(city_id)
    return redirect('detail', trip_id=trip_id)