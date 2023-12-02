from django.db import models
from mercado_local_app.models  import Cliente
from productos_app.models import Producto


# Create your models here.

class Orden(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta = models.ForeignKey('Venta', null=True, on_delete=models.CASCADE)
    cantidadProducto = models.IntegerField(null=False, blank=False)
    costoOrden = models.IntegerField(null=False, blank=False)
    en_carrito = models.BooleanField(default=True)

class Venta(models.Model):
    costoTotal = models.IntegerField(null=False, blank=False)
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
    ordenes = models.ManyToManyField(Orden, related_name='ventas')

class HistorialCompra(models.Model):
    producto = models.ForeignKey(Producto, null=False, on_delete=models.PROTECT)
    costoCompra = models.IntegerField(null=False, blank=False)
    venta = models.ForeignKey(Venta, null=True, on_delete=models.SET_NULL)
    orden = models.ForeignKey(Orden, null=True, on_delete=models.SET_NULL)