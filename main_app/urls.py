from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('countries/', views.countries_index, name='countries_index'),
    path('trips/', views.trips_index, name='trips_index'),
    path('countries/<int:country_id>/', views.countries_detail, name='country_detail'),
    path('trips/<int:trip_id>/', views.trips_detail, name='trip_detail'),
    path('countries/create/', views.CountryCreate.as_view(), name='countries_create'),
    path('trips/create/', views.TripCreate.as_view(), name='trips_create'),
    path('cities/create/', views.CityCreate.as_view(), name='cities_create'),
    path('countries/<int:pk>/update/', views.CountryUpdate.as_view(), name='countries_update'),
    path('trips/<int:trip_id>/assoc_country/<int:country_id>/', views.assoc_country, name='assoc_country'),
    path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trips_update'),
    path('trips/<int:trip_id>/assoc_city/<int:city_id>/', views.assoc_city, name='assoc_city'),
    path('countries/<int:pk>/delete/', views.CountryDelete.as_view(), name='countries_delete'),
    path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trips_delete'),
]