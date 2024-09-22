from django.db import models
from autenticacion.models import User
class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=10, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')])

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"