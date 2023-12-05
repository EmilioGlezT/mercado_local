from django.http import HttpResponse
from django.shortcuts import render
from productos_app.models import Producto
from mercado_local_app.models import Negocio
from .forms import RegistroProducto
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.urls import reverse_lazy


class RegistroProducto(FormView):
    template_name = 'registroProducto.html' 
    form_class = RegistroProducto
    success_url = reverse_lazy('') 

    def form_valid(self, form):
        form.save()  
        return super().form_valid(form)

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ["nombreProducto", "precio", "existencias"]
    template_name = "producto_update_form.html"  # Ruta correcta
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('home')


    
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "producto_confirm_delete.html"  # Ruta correcta
    success_url = reverse_lazy("home")
