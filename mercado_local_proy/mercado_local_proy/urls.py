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
from django.urls import path
from mercado_local_app.views import UsersListView, VendedoresListView, ClientesListView
from mercado_local_app import views
import mercado_local_app.views
from registro_productos import views
import registro_productos.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mercado_local_app.views.index, name="index"),
    path('getAllUsers/',UsersListView.as_view()),
    path('getAllVendedores/',VendedoresListView.as_view()),
    path('getAllClientes/',ClientesListView.as_view()),
    path('createProduct/' , registro_productos.views.createProducto, name = "create"),
    path('crear-producto/', registro_productos.views.crearProduto),
    path('save-product', registro_productos.views.saveProducto, name= 'save')
]
