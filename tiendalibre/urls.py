from django.urls import path
from . import views

app_name = 'tiendalibre'

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),
]
