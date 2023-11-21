from django.db import models
from mercado_local_app.models  import Negocio, Cliente

# Create your models here.


class Producto(models.Model):
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE, related_name='productos')
    nombreProducto = models.CharField(max_length=30, null=False, blank=False)
    descripcionProducto = models.CharField(max_length=30, null=False, blank=False)
    imagenProducto = models.ImageField(default="null")
    categoria = models.CharField(max_length=30)  
    precio = models.FloatField()

class Venta(models.Model):
    costoTotal = models.IntegerField(null=False, blank=False)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE )

class Orden(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta =  models.ForeignKey(Venta, null=True, on_delete=models.CASCADE)
    cantidadProducto = models.IntegerField(null=False, blank=False)
    costoOrden = models.IntegerField(null=False, blank=False)



class HistorialCompra(models.Model):
    producto = models.ForeignKey(Producto, null=False, on_delete=models.PROTECT)
    costoCompra = models.IntegerField(null=False, blank=False)
    venta = models.ForeignKey(Venta, null=True, on_delete=models.SET_NULL)
    orden = models.ForeignKey(Orden, null=True, on_delete=models.SET_NULL)
    
