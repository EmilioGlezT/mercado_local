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
  
    carrito = Orden.objects.filter(venta__isnull=True)

    subtotal = sum(orden.costoOrden for orden in carrito)
    
    context = {'carrito': carrito, 'subtotal': subtotal}
    
    return render(request, 'compra_app/carrito.html', context)

def agregar_al_carrito(request, producto_id):

    producto = Producto.objects.get(id=producto_id)
    

    orden, creado = Orden.objects.get_or_create(
        producto=producto,
        en_carrito=True,
        defaults={'cantidadProducto': 1, 'costoOrden': producto.precio}
    )

    if not creado:
     
        orden.cantidadProducto += 1
        orden.costoOrden += producto.precio
        orden.save()


    return redirect('compra_app:ver_carrito')

def eliminar_del_carrito(request, orden_id):
    
    orden = Orden.objects.get(id=orden_id)
    
    
    orden.delete()

   
    return redirect('compra_app:ver_carrito')

def modificar_cantidad_carrito(request, orden_id, operacion):
  
    orden = Orden.objects.get(id=orden_id)

 
    if operacion == 'sumar':
        orden.cantidadProducto += 1
    elif operacion == 'restar':
        if orden.cantidadProducto > 1:
            orden.cantidadProducto -= 1

 
    orden.costoOrden = orden.cantidadProducto * orden.producto.precio
    orden.save()

   
    return redirect('compra_app:ver_carrito')