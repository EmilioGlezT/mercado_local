from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from productos_app.models import Producto
from compra_app.models import Orden, Venta , HistorialCompra
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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


@login_required
def procesar_pago(request):
 
    carrito = Orden.objects.filter(venta__isnull=True)

    if not carrito.exists():

        return redirect('compra_app:ver_carrito')


    for orden in carrito:
        producto = orden.producto
        if orden.cantidadProducto > producto.existencias:
     
            return render(request, 'compra_app/error_disponibilidad.html', {'producto': producto})

      
        producto.existencias -= orden.cantidadProducto
        producto.save()


    costo_total = sum(orden.costoOrden for orden in carrito)


    cliente = request.user.userprofile

    venta = Venta.objects.create(
        cliente=cliente,
        costoTotal=costo_total
    )

    venta.save()
   
    for orden in carrito:
        orden.venta = venta
        orden.en_carrito = False
        orden.save()

        HistorialCompra.objects.create(
            producto=orden.producto,
            costoCompra=orden.costoOrden,
            venta=venta,
            orden=orden
        )


    ordenes_asociadas = Orden.objects.filter(venta=venta)

    return render(request, 'compra_app/confirmacion_pago.html', {'venta': venta, 'ordenes_asociadas': ordenes_asociadas})

def error_disponibilidad(request):
    return render(request, 'compra_app/error_disponibilidad.html')

def historial_compras(request):

    historial_compras = HistorialCompra.objects.filter(venta__cliente=request.user.userprofile)

    return render(request, 'compra_app/historial_compras.html', {'historial_compras': historial_compras})