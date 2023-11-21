from django.contrib import admin

# Register your models here.
from .models import CustomUser, Vendedor, Negocio, Cliente
# Register your models here.
@admin.register(CustomUser, Vendedor, Negocio, Cliente)

class CustomAdmin(admin.ModelAdmin):
    pass