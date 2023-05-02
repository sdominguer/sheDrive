from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    telefono=models.CharField(max_length=10)

class Conductora(models.Model):
    nombre=models.CharField(max_length=30)
    correo=models.EmailField()
    telefono=models.CharField(max_length=10)
    contraseña=models.CharField(max_length=60)
    identificacion= models.CharField(max_length=20)

class Viaje(models.Model):
    #identificacionUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, to_field="username")
    #identificacionConductora=models.ForeignKey(Conductora, on_delete=models.CASCADE, to_field="identificacion")
    origen=models.CharField(max_length=30)
    destino=models.CharField(max_length=30)
    precio=models.FloatField()
    distancia = models.IntegerField()
    tiempo=models.CharField(max_length=30)

class Vehiculo(models.Model):
    marca=models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)
    papeles=models.CharField(max_length=30)