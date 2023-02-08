from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Country
from .forms import VisitForm
 


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
  visit_form = VisitForm()
  return render(request, 'countries/detail.html', { 
    'country': country,
    'visit_form': visit_form 
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

def add_visit(request, country_id):
  form = VisitForm(request.POST)
  if form.is_valid():
    new_visit = form.save(commit=False)
    new_visit.country_id = country_id
    new_visit.save()
  return redirect('detail', country_id=country_id)