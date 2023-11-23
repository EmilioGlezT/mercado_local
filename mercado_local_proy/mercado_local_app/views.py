from django.shortcuts import render
import datetime
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import CustomUser
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


def login_view(request):
    return render(request, 'login.html')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# def register_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('pagina_inicio')

#     else:
#         form = CustomUserCreationForm()

#     return render(request, 'register.html', {'form': form})

