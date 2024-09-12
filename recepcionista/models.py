from django.db import models

# Create your models here.
class Recepcionista(models.Model):
    usuario = models.ForeignKey('autenticacion.Usuario', on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=10, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')])

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"  # Nombre completo desde el modelo Usuario