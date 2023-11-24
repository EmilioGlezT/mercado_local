from django.shortcuts import render
from django.views.generic import ListView, DetailView
from productos_app.models import Producto

# Create your views here.
class Catalogo_ListView(ListView):
    template_name = 'productos_app/catalogo_producto.html'
    context_object_name = 'catalogo_principal'

    def get_queryset(self):
        return Producto.objects.all()
    
class DetalleProductoView(DetailView):
    model = Producto
    template_name = "productos_app/detalle_producto.html"