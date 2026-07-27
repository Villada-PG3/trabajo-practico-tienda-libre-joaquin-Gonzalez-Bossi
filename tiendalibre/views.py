from django.shortcuts import render

from django.views.generic import TemplateView

class TiendaTemplateView(TemplateView):
    template_name = 'tienda.html'
# Create your views here.
