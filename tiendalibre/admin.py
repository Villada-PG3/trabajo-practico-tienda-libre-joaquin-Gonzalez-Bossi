from django.contrib import admin
from .models import Producto,Categoria
from django.utils.html import format_html



@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'mostrar_miniatura')
    
    readonly_fields = ('mostrar_imagen_detalle',)

    def mostrar_miniatura(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="50" height="50" />',obj.imagen.url)
        return "sin imagen"
    
    mostrar_miniatura.short_description = 'Miniatura'
    
    def mostrar_imagen_detalle(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="300" height="300" />',obj.imagen.url)
        return "sin imagen"
    
    mostrar_imagen_detalle.short_description = 'Previsualización de la imagen'

admin.site.register(Categoria)
