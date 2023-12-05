from django.contrib import admin

# Register your models here.
from .models import UserProfile, Negocio
from productos_app.models import Producto
from compra_app.models import Venta, HistorialCompra, Orden
# Register your models here.
@admin.register(UserProfile,  Negocio,  Producto, Venta, HistorialCompra, Orden)

class CustomAdmin(admin.ModelAdmin):
    pass