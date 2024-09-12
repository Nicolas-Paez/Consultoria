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

    # Indicar que el campo rut será utilizado como el nombre de usuario
    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'rol']  # Campos obligatorios adicionales

    def __str__(self):
        return self.rut  # Devolver el rut como representación del usuario