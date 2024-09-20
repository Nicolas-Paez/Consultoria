from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

class Terapeuta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    especialidad = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=10, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')])
    disponibilidad = models.CharField(max_length=30, choices=[('Disponible', 'Disponible'), ('Medianamente Disponible', 'Medianamente Disponible'), ('No Disponible', 'No Disponible')])
    horas_trabajadas = models.FloatField(default=0)
    '''
    @property
    def nombre_completo(self):
        return f"{self.user.first_name} {self.user.last_name}"'''


class citas(models.Model):
    id_terapeuta = models.ForeignKey(Terapeuta, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    sala = models.CharField(max_length=50)
    detalle = models.CharField(max_length=100)

class Horario(models.Model):
    id_terapeuta = models.ForeignKey('Terapeuta', on_delete=models.CASCADE)
    lunes_am_ini = models.TimeField()
    lunes_am_fin = models.TimeField()
    lunes_pm_ini = models.TimeField()
    lunes_pm_fin = models.TimeField()
    martes_am_ini = models.TimeField()
    martes_am_fin = models.TimeField()
    martes_pm_ini = models.TimeField()
    martes_pm_fin = models.TimeField()
    miercoles_am_ini = models.TimeField()
    miercoles_am_fin = models.TimeField()
    miercoles_pm_ini = models.TimeField()
    miercoles_pm_fin = models.TimeField()
    jueves_am_ini = models.TimeField()
    jueves_am_fin = models.TimeField()
    jueves_pm_ini = models.TimeField()
    jueves_pm_fin = models.TimeField()
    viernes_am_ini = models.TimeField()
    viernes_am_fin = models.TimeField()
    viernes_pm_ini = models.TimeField()
    viernes_pm_fin = models.TimeField()
    sabado_am_ini = models.TimeField()
    sabado_am_fin = models.TimeField()
    sabado_pm_ini = models.TimeField()
    sabado_pm_fin = models.TimeField()
    domingo_am_ini = models.TimeField()
    domingo_am_fin = models.TimeField()
    domingo_pm_ini = models.TimeField()
    domingo_pm_fin = models.TimeField()

    def calcular_horas_totales(self):
        # Calcular horas de un periodo (AM o PM) de un día
        def calcular_horas(ini, fin):
            if ini and fin:
                inicio = timedelta(hours=ini.hour, minutes=ini.minute)
                final = timedelta(hours=fin.hour, minutes=fin.minute)
                return (final - inicio).total_seconds() / 3600
            return 0

        # Sumamos las horas trabajadas en cada día (AM + PM)
        horas_trabajadas = 0
        horas_trabajadas += calcular_horas(self.lunes_am_ini, self.lunes_am_fin)
        horas_trabajadas += calcular_horas(self.lunes_pm_ini, self.lunes_pm_fin)
        horas_trabajadas += calcular_horas(self.martes_am_ini, self.martes_am_fin)
        horas_trabajadas += calcular_horas(self.martes_pm_ini, self.martes_pm_fin)
        horas_trabajadas += calcular_horas(self.miercoles_am_ini, self.miercoles_am_fin)
        horas_trabajadas += calcular_horas(self.miercoles_pm_ini, self.miercoles_pm_fin)
        horas_trabajadas += calcular_horas(self.jueves_am_ini, self.jueves_am_fin)
        horas_trabajadas += calcular_horas(self.jueves_pm_ini, self.jueves_pm_fin)
        horas_trabajadas += calcular_horas(self.viernes_am_ini, self.viernes_am_fin)
        horas_trabajadas += calcular_horas(self.viernes_pm_ini, self.viernes_pm_fin)
        horas_trabajadas += calcular_horas(self.sabado_am_ini, self.sabado_am_fin)
        horas_trabajadas += calcular_horas(self.sabado_pm_ini, self.sabado_pm_fin)
        horas_trabajadas += calcular_horas(self.domingo_am_ini, self.domingo_am_fin)
        horas_trabajadas += calcular_horas(self.domingo_pm_ini, self.domingo_pm_fin)

        return horas_trabajadas

    