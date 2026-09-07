from datetime import date

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView

from .models import Producto
from django.shortcuts import get_object_or_404

class TiendaTemplateView(TemplateView):
    template_name = 'tienda.html'

def home_1(request):
    return HttpResponse("<h1>Bienvenido a la tienda Libre de Maximo Corallo Margosian</h1>")

def home(request):
    productos_recientes = Producto.objects.filter(activo=True).order_by('-id')[:3]
    productos_destacados = Producto.objects.filter(activo=True)[:6]

    contexto = {
        'titulo': 'Ofertas de la semana',
        'productos_recientes': productos_recientes,
        'usuario_logueado': True,
        'esta_logueado': True,
        'fecha_actualizacion': date(2026, 7, 20),
        'productos_destacados': productos_destacados,
    }
    return render(request, 'tiendalibre/home.html', contexto)

def acerca_de_mi(request):
    return render(request, 'tiendalibre/acerca-de-mi.html')


def catalogo(request):
    productos = Producto.objects.filter(activo=True).order_by('-nombre')
    contexto = {
        'productos': productos,
    }
    return render(request, 'tiendalibre/catalogo.html', contexto)

def detalle_producto(request, pk):
    producto = Producto.objects.filter(pk=pk)
    producto = get_object_or_404(Producto, pk=pk)
    contexto = {'producto': producto,}
    return render(request, 'tiendalibre/producto_detalle.html', contexto)