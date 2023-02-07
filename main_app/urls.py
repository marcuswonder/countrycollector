from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('countries/', views.countries_index, name='index'),
    path('countries/<int:country_id>/', views.countries_detail, name='detail'),
]