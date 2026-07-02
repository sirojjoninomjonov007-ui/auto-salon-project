from django.urls import path
from apps.autosalon.views import car_list
from .models import views

urlpatterns = [
    path('cars/', views.car_list, name='car_list'),
    

]