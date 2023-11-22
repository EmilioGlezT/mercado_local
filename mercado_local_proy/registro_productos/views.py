from django.http import HttpResponse
from django.shortcuts import render
from productos_app.models import Producto


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
    crearProduto.save()
    return HttpResponse(f"Producto creado: <strong>{producto.nombreProducto}" )
    
def saveProducto(request):
    producto = Producto(
    negocio = negocio,
    nombreProducto = nombreProducto,
    descripcionProducto = descripcionProducto,
    imagenProducto = imagenProducto,
    precio = precio
    )
    crearProduto.save()
    return HttpResponse(f"Producto creado: <strong>{producto.nombreProducto}" )

def createProducto(request):
    return render(request, 'createProduct.html')
        

# Create your views here.
