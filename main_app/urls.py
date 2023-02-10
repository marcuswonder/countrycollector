from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('countries/', views.countries_index, name='countries_index'),
    path('trips/', views.trips_index, name='trips_index'),
    path('segments/', views.segments_index, name='segments_index'),
    path('countries/<int:country_id>/', views.countries_detail, name='country_detail'),
    path('trips/<int:trip_id>/', views.trips_detail, name='trip_detail'),
    path('segments/<int:segment_id>/', views.segments_detail, name='segment_detail'),
    path('countries/create/', views.CountryCreate.as_view(), name='countries_create'),
    path('trips/create/', views.TripCreate.as_view(), name='trips_create'),
    path('segments/create/', views.SegmentCreate.as_view(), name='segments_create'),
    path('countries/<int:pk>/update/', views.CountryUpdate.as_view(), name='countries_update'),
    path('trips/<int:trip_id>/assoc_country/<int:country_id>/', views.assoc_country, name='assoc_country'),
    path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trips_update'),
    path('trips/<int:trip_id>/segment/<int:segment_id>/', views.assoc_segment, name='assoc_segment'),
    path('segments/<int:pk>/update/', views.SegmentUpdate.as_view(), name='segments_update'),
    path('countries/<int:pk>/delete/', views.CountryDelete.as_view(), name='countries_delete'),
    path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trips_delete'),
    path('segments/<int:pk>/delete/', views.SegmentDelete.as_view(), name='segments_delete'),
    path('fetchcountries', views.fetchCountries, name='fetch_countries')
]
# Not sure if the path(s) below are necessary any more:
# path('trips/<int:trip_id>/assoc_country/<int:country_id>/', views.assoc_country, name='assoc_country'),