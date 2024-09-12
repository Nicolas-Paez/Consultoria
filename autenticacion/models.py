from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Usuario(AbstractUser):
    class Roles(models.TextChoices):
        ADMINISTRADOR = 'Administrador'
        RECEPCIONISTA = 'Recepcionista'
        TERAPEUTA = 'Terapeuta'
    
    rol = models.CharField(max_length=20, choices=Roles.choices, default=Roles.RECEPCIONISTA)
    rut = models.CharField(max_length=12, unique=True)
    cotrasena = models.CharField(max_length=100)