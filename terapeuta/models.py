from django.db import models

class Terapeuta(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    especialidad = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=10, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')])


class citas(models.Model):
    id_terapeuta = models.ForeignKey(Terapeuta, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    sala = models.CharField(max_length=50)
    detalle = models.CharField(max_length=100)