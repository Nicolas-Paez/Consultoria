from django.db import models

class Terapeuta(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    especialidad = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=10, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')])
