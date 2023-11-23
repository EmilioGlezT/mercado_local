from django.contrib import admin

# Register your models here.
from .models import CustomUser, Vendedor, Negocio, Cliente
from productos_app.models import Producto
# Register your models here.
@admin.register(CustomUser, Vendedor, Negocio, Cliente, Producto)

class CustomAdmin(admin.ModelAdmin):
    pass