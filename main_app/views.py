from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Country
from .forms import TripForm
 


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def countries_index(request):
  countries = Country.objects.all()
  return render(request, 'countries/index.html', { 'countries': countries })

def countries_detail(request, country_id):
  country = Country.objects.get(id=country_id)
  trip_form = TripForm()
  return render(request, 'countries/detail.html', { 
    'country': country,
    'trip_form': trip_form 
  })

class CountryCreate(CreateView):
  model = Country
  fields = '__all__'

class CountryUpdate(UpdateView):
  model = Country
  fields = '__all__'

class CountryDelete(DeleteView):
  model = Country
  success_url = '/countries'

def add_trip(request, country_id):
  form = TripForm(request.POST)
  if form.is_valid():
    new_trip = form.save(commit=False)
    new_trip.country_id = country_id
    new_trip.save()
  return redirect('detail', country_id=country_id)