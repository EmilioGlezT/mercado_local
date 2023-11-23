from django.db import models
from mercado_local_app.models  import Negocio, Cliente
from productos_app.models import Producto


# Create your models here.
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