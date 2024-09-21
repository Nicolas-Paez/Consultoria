from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recepcionista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    fecha_contratacion = models.DateField()
    turno = models.CharField(max_length=100, null=True, choices=[('M', 'Mañana'), ('T', 'Tarde'), ('N', 'Noche')])
    experiencia = models.IntegerField(null=True, blank=True)
    formacion_academica = models.CharField(max_length=100, null=True)
    supervisor = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"