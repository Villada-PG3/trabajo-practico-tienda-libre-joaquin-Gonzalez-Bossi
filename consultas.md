# Consultas ORM de Django

Para abrir el shell desde la carpeta del proyecto:

```bash
python manage.py shell
```

Importamos los modelos:

```python
from tiendalibre.models import Producto, Categoria
```

## 1. Obtener todos los productos

`all()` devuelve un `QuerySet` con todos los productos. La consulta se ejecuta cuando lo recorremos o mostramos.

```python
productos = Producto.objects.all()
list(productos)
```

## 2. Filtrar por marca

`filter()` devuelve un `QuerySet`, aunque haya cero, uno o muchos resultados.

```python
Producto.objects.filter(marca="Coca-Cola")
```

## 3. Buscar nombres sin distinguir mayúsculas

El lookup `__icontains` busca un texto dentro del campo sin distinguir mayúsculas y minúsculas.

```python
Producto.objects.filter(nombre__icontains="agua")
```

## 4. Buscar productos con precio mayor a un valor

El lookup `__gt` significa greater than, es decir, mayor que.

```python
Producto.objects.filter(precio__gt=3000)
```

## 5. Buscar productos con stock menor a un valor

El lookup `__lt` significa less than, es decir, menor que.

```python
Producto.objects.filter(stock__lt=20)
```

## 6. Filtrar por varios valores posibles

El lookup `__in` devuelve productos cuyo campo coincide con alguno de los valores de la lista.

```python
Producto.objects.filter(marca__in=["Coca-Cola", "Villavicencio", "Alicante"])
```

## 7. Excluir y ordenar resultados

`exclude()` elimina los productos que cumplen la condición. `order_by()` ordena el resultado; el signo `-` indica orden descendente.

```python
Producto.objects.exclude(stock=0).order_by("-precio")
```

## 8. Obtener un único producto con `get()`

`get()` debe encontrar exactamente un objeto. Si no encuentra ninguno lanza `DoesNotExist`; si encuentra más de uno lanza `MultipleObjectsReturned`.

```python
producto = Producto.objects.get(nombre="Agua")
producto.precio
```

A diferencia de `filter()`, `get()` devuelve un objeto `Producto`, no un `QuerySet`.

## 9. Navegar la relación entre producto y categoría

Desde un producto accedemos a su categoría mediante `categoria`. Desde una categoría accedemos a sus productos mediante el `related_name` `productos`.

```python
producto = Producto.objects.exclude(categoria=None).first()
producto.categoria.nombre

categoria = Categoria.objects.first()
categoria.productos.all()
```

## 10. Crear un producto desde el shell

`create()` crea y guarda el producto en la base de datos en una sola operación. La categoría es opcional porque el modelo permite valores nulos.

```python
producto_nuevo = Producto.objects.create(
    nombre="Producto de prueba",
    descripcion="Creado desde Django shell",
    precio=1999.99,
    stock=10,
    marca="Marca de prueba",
)
producto_nuevo
```

Para borrar el producto de prueba después de revisarlo:

```python
producto_nuevo.delete()
```
