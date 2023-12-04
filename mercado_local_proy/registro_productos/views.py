from django.http import HttpResponse
from django.shortcuts import render
from productos_app.models import Producto
from mercado_local_app.models import Negocio
from .forms import RegistroProducto
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

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
    if request.method == 'POST':
        """negocio = request.GET.get('negocio')"""

        negocioid = 1
        negocio = Negocio.objects.get(id=negocioid)
        nombreProducto = request.POST.get('nombreProducto')
        descripcionProducto = request.POST.get('descripcionProducto')
        imagenProducto = request.POST.get('imagenProducto')
        categoria = request.POST.get('categoria')
        precio = request.POST.get('precio')     

        producto = Producto(
        negocio = negocio,
        nombreProducto = nombreProducto,
        categoria = categoria,
        descripcionProducto = descripcionProducto,
        imagenProducto = imagenProducto,
        precio = precio
        )
        producto.save()
        
   

def createProducto(request):
    return render(request, 'createProduct.html')
        

class RegistroProducto(FormView):
    template_name = 'registroProducto.html'  # Reemplaza 'tu_template.html' con la plantilla que deseas utilizar
    form_class = RegistroProducto
    success_url = reverse_lazy('producto')  # Reemplaza 'nombre_de_la_url_de_exito' con el nombre de la URL a la que redirigir después del registro

    def form_valid(self, form):
        form.save()  # Esto guarda el nuevo usuario en la base de datos
        return super().form_valid(form)
