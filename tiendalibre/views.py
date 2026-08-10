from django.shortcuts import render
from django.views.generic import TemplateView


class TiendaTemplateView(TemplateView):
    template_name = 'tienda.html'


def home(request):
    return render(request, 'tiendalibre/home.html')


def acerca_de_mi(request):
    return render(request, 'tiendalibre/acerca-de-mi.html')