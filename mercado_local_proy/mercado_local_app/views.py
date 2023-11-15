from django.shortcuts import render, redirect, HttpResponse
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy



from mercado_local_app.models import Producto, CustomUser


def pagina_inicio(request):
    return render(request, 'inicio.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('pagina_inicio')

    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def crear_producto(request):
    return HttpResponse("Producto creado")

# Create your views here.
