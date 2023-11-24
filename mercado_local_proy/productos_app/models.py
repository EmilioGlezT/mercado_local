from django.db import models
from mercado_local_app.models  import Negocio

# Create your models here.


class Producto(models.Model):
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE, related_name='productos')
    nombreProducto = models.CharField(max_length=30, null=False, blank=False)
    descripcionProducto = models.CharField(max_length=30, null=False, blank=False)
    imagenProducto = models.ImageField(default="null")
    categoria = models.CharField(max_length=30)  
    precio = models.FloatField()
    existencias = models.IntegerField(null=False, default=0)


    
