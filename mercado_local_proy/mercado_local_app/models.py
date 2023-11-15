from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    location = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=400, null=True, blank=True)
    image = models.ImageField(default="null")
    CLIENTE = 'cliente'
    VENDEDOR = 'vendedor'
    
    USER_TYPE_CHOICES = [
        (CLIENTE, 'Cliente'),
        (VENDEDOR, 'Vendedor'),
    ]

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default=CLIENTE,
    )
    

class Producto(models.Model):
    vendedor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='productos')
    nombreProducto = models.CharField(max_length=30, null=False, blank=False)
    descripcionProducto = models.CharField(max_length=30, null=False, blank=False)
    imagenProducto = models.ImageField(default="null")
    categoria = models.CharField(max_length=30)  
    precio = models.FloatField()


    

