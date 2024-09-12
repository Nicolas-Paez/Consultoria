from django.db import models

class Administrador(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=10, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')])

    def __str__(self):
        return self.nombre