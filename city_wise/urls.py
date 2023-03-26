from django.contrib import admin
from django.urls import path
from city_wise import views

urlpatterns = [
    path('', views.index, name='home'),
    path('404', views.index, name='error'),
    
]