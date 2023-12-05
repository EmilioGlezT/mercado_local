from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView
from mercado_local_app.forms.forms import  RegisterForm, RegistroForm
from mercado_local_app.models import  UserProfile
from django.contrib.auth import login




# Clases genericas ListView Se utilizan para traer un listado completo de un modelo

class UsersListView(ListView):
    model = User
    template_name="ListViewsTemplates/ListUsers.html"

# class VendedoresListView(ListView):
#     model = Vendedor
#     template_name="ListViewsTemplates/ListVendedores.html"

# class ClientesListView(ListView):
#     model = Cliente
#     template_name="ListViewsTemplates/ListCLientes.html"
    
class RegistroUsuarioView(FormView):
    template_name = 'registroDatosExtra.html'  # Reemplaza 'tu_template.html' con la plantilla que deseas utilizar
    form_class = RegisterForm
    success_url = reverse_lazy('home')  # Reemplaza 'nombre_de_la_url_de_exito' con el nombre de la URL a la que redirigir después del registro

    def form_valid(self, form):
        form.save()  # Esto guarda el nuevo usuario en la base de datos
        return super().form_valid(form)

class RegistroView(View):
    template_name = 'registroUser.html'
    form_class = RegistroForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('registro_datosExtra')  # Cambia 'inicio' al nombre de la URL a la que deseas redirigir después del registro exitoso
        return render(request, self.template_name, {'form': form})




