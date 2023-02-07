from django.shortcuts import render

countries = [
    {'name': 'USA', 'continent': 'North America', 'region': 'North America', 'capital_city': 'Washington DC', 'population': 331900000},
    {'name': 'England', 'continent': 'Europe', 'region': 'Western Europe', 'capital_city': 'London', 'population': 55980000},
    {'name': 'Sierra Leone', 'continent': 'Africa', 'region': 'West Africa', 'capital_city': 'Freetown', 'population': 8421000},
]   
    


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def countries_index(request):
  return render(request, 'countries/index.html', {
    'countries': countries
  })

