from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from productos_app.models import Producto
from compra_app.models import Orden 

# Create your views here.
##
##class Carrito_ListView(ListView):
  ##  template_name = 'compra_app/carrito.html'
    ##context_object_name = 'carrito'

    ##def get_queryset(self):
      ##  return Orden.objects.all()

def ver_carrito(request):
    # Obtener todas las órdenes en el carrito
    carrito = Orden.objects.filter(venta__isnull=True)
    
    context = {'carrito': carrito}
    return render(request, 'compra_app/carrito.html', context)

def agregar_al_carrito(request, producto_id):
    # Obtener el producto a agregar al carrito
    producto = Producto.objects.get(id=producto_id)
    
    # Obtener o crear la orden en el carrito para ese producto
    orden, creado = Orden.objects.get_or_create(
        producto=producto,
        en_carrito=True,
        defaults={'cantidadProducto': 1, 'costoOrden': producto.precio}
    )

    if not creado:
        # Si la orden ya existe en el carrito, aumentar la cantidad y actualizar el costo
        orden.cantidadProducto += 1
        orden.costoOrden += producto.precio
        orden.save()

    # Redirigir a la página de detalle del producto o a donde desees
    return redirect('compra_app:ver_carrito')