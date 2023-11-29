from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from productos_app.models import Producto
from compra_app.models import Orden 

# Create your views here.
class Carrito_ListView(ListView):
    template_name = 'compra_app/carrito.html'
    context_object_name = 'carrito'

    def get_queryset(self):
        return Orden.objects.all()