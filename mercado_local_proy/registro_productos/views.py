from django.http import HttpResponse
from django.shortcuts import render
from productos_app.models import Producto
from mercado_local_app.models import Negocio


def registrarProductos(request):
    return render(request, 'registrarProductos.html')

def crearProduto(request, negocio, nombreProducto, descripcionProducto, imagenProducto, precio):
    producto = Producto(
    negocio = negocio,
    nombreProducto = nombreProducto,
    descripcionProducto = descripcionProducto,
    imagenProducto = imagenProducto,
    precio = precio
    )
    producto.save()
    return HttpResponse(f"Producto creado: <strong>{producto.nombreProducto}" )
    
def saveProducto(request):
    if request.method == 'GET':
        """negocio = request.GET.get('negocio')"""

        negocioid = 1
        negocio = Negocio.objects.get(id=negocioid)
        nombreProducto = request.GET.get('nombreProducto')
        descripcionProducto = request.GET.get('descripcionProducto')
        imagenProducto = request.GET.get('imagenProducto')
        precio = request.GET.get('precio')     

        producto = Producto(
        negocio = negocio,
        nombreProducto = nombreProducto,
        descripcionProducto = descripcionProducto,
        imagenProducto = imagenProducto,
        precio = precio
        )
        producto.save()
        return HttpResponse(f"Producto creado: <strong>{producto.nombreProducto}" )
    else:
        return HttpResponse("<h2>No se pudo crear el producto</h2>")

def createProducto(request):
    return render(request, 'createProduct.html')
        

# Create your views here.
