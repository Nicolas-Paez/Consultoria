from django.db import models

class Administrador(models.Model):
    usuario = models.ForeignKey('autenticacion.Usuario', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=10, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')])

    def __str__(self):
        return self.nombre + ' ' + self.apellidos