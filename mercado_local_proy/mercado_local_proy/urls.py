"""
URL configuration for mercado_local_proy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from mercado_local_app.views import UsersListView, VendedoresListView, ClientesListView, RegistroUsuarioView, RegistroVendedor, RegistroCliente
from mercado_local_app import views
import mercado_local_app.views

import registro_productos.views


urlpatterns = [
    path('admin/', admin.site.urls),

    # app listado productos
    path('productos/', include('productos_app.urls')),


    
    
  

    # app registro, eliminacion, creacion producto
    # path('productoreg/', include('registro_productos.urls')), 
    path('createProduct/' , registro_productos.views.createProducto, name = "create"),
    path('crear-producto/', registro_productos.views.crearProduto),
    path('save-product', registro_productos.views.saveProducto, name= 'save'),


    # app usuario y login
    
     
    path('getAllUsers/',UsersListView.as_view()),
    path('getAllVendedores/',VendedoresListView.as_view()),
    path('getAllClientes/',ClientesListView.as_view()),
    path('cuentas/', include("django.contrib.auth.urls")),


    path('registro/', RegistroUsuarioView.as_view(), name='registro_usuario'),
    path('registroVendedor/', RegistroVendedor.as_view(), name='registro_vendedor'),
     path('registroCliente/', RegistroCliente.as_view(), name='registro_cliente'),
    #paginas principales
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("info/", TemplateView.as_view(template_name="info.html"), name="info"),   



]
