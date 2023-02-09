from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('countries/', views.countries_index, name='countries_index'),
    path('trips/', views.trips_index, name='trips_index'),
    path('countries/<int:country_id>/', views.countries_detail, name='detail'),
    path('trips/<int:trip_id>/', views.trips_detail, name='detail'),
    path('countries/create/', views.CountryCreate.as_view(), name='countries_create'),
    path('trips/new/', views.new_trip, name='new_trip'),
    path('countries/<int:pk>/update/', views.CountryUpdate.as_view(), name='countries_update'),
    path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trips_update'),
    path('countries/<int:pk>/delete/', views.CountryDelete.as_view(), name='countries_delete'),
    path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trips_delete'),
    path('trips/new', views.add_trip, name='add_trip'),
]