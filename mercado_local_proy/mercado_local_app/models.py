from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

# Create your models here.


class Negocio(models.Model):
    nombre = models.CharField()
    razonSocial = models.CharField(max_length=14, null= False, blank=False)
    ciudad = models.CharField(max_length=30,null=False, blank=False)
    estado = models.CharField(max_length=30, null=False, blank=False)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    calle = models.CharField(max_length=50, null=False, blank=False, default="")
    colonia = models.CharField(max_length=50, null=False, blank=False, default="")
    codigoPostal = models.IntegerField(null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True) 
    bio = models.TextField(max_length=400, null=True, blank=True)
    image = models.ImageField(default="null")
    is_cliente = models.BooleanField(default=False)
    is_vendedor = models.BooleanField(default=False)
    negocio = models.ForeignKey(Negocio, null=True, blank=False, on_delete=models.SET_NULL)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.user.username
