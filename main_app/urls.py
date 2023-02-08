from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('countries/', views.countries_index, name='index'),
    path('countries/<int:country_id>/', views.countries_detail, name='detail'),
    path('countries/create/', views.CountryCreate.as_view(), name='countries_create'),
    path('countries/<int:pk>/update/', views.CountryUpdate.as_view(), name='countries_update'),
    path('countries/<int:pk>/delete/', views.CountryDelete.as_view(), name='countries_delete'),
    path('countries/<int:country_id>/add_trip/', views.add_trip, name='add_trip'),
]