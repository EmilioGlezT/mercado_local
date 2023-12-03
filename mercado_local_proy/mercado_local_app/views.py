from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import CustomUser
from mercado_local_app.forms.forms import  RegisterForm, RegisterVendedorForm, RegisterClienteForm
from mercado_local_app.models import  CustomUser, Vendedor, Cliente




# Clases genericas ListView Se utilizan para traer un listado completo de un modelo

class UsersListView(ListView):
    model = CustomUser
    template_name="ListViewsTemplates/ListUsers.html"

class VendedoresListView(ListView):
    model = Vendedor
    template_name="ListViewsTemplates/ListVendedores.html"

class ClientesListView(ListView):
    model = Cliente
    template_name="ListViewsTemplates/ListCLientes.html"
    
class RegistroUsuarioView(FormView):
    template_name = 'registroCustomUser.html'  # Reemplaza 'tu_template.html' con la plantilla que deseas utilizar
    form_class = RegisterForm
    success_url = reverse_lazy('home')  # Reemplaza 'nombre_de_la_url_de_exito' con el nombre de la URL a la que redirigir después del registro

    def form_valid(self, form):
        form.save()  # Esto guarda el nuevo usuario en la base de datos
        return super().form_valid(form)


class RegistroVendedor(FormView):
    template_name = 'registroVendedor.html'
    form_class = RegisterVendedorForm
    def form_valid(self, form):
        form.save()  # Esto guarda el nuevo usuario en la base de datos
        return super().form_valid(form)
    
class RegistroCliente(FormView):
    template_name = "registroCliente.html"
    form_class = RegisterClienteForm
    def form_valid(self, form):
        form.save()  # Esto guarda el nuevo usuario en la base de datos
        return super().form_valid(form)
