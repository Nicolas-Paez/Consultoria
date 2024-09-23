from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

class Terapeuta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    especialidad = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=10, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')])
    disponibilidad = models.CharField(max_length=30, choices=[('Disponible', 'Disponible'), ('Medianamente Disponible', 'Medianamente Disponible'), ('No Disponible', 'No Disponible')])
    horas_trabajadas = models.FloatField(default=0)
    fecha_contratacion = models.DateField()
    titulo = models.CharField(max_length=100, default="Sin título")
    experiencia = models.IntegerField(null=True, blank=True)
    presentacion = models.CharField(max_length=500, default="¡Hola! Soy tu terapeuta. Estoy aquí para ayudarte a mejorar tu calidad de vida. ¡Vamos a trabajar juntos!") 
    correo_contacto = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    terapeuta = models.ForeignKey(Terapeuta, on_delete=models.CASCADE, null=True, blank=True)
    contacto_emergencia = models.CharField(max_length=100)
    telefono_emergencia = models.CharField(max_length=12)
    historial_medico = models.TextField()
    medicamentos = models.CharField(max_length=500)
    patologia = models.CharField(max_length=100)
    alergias = models.CharField(max_length=100)
    progreso = models.TextField()
    dispositivo_ortesis = models.CharField(max_length=100)
    actividad_fisica = models.CharField(max_length=100, choices=(("Sedentario", "Sedentario"), ("Moderado", "Moderado"), ("Activo", "Activo")))
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    imc = models.DecimalField(max_digits=5, decimal_places=2)
    motivo_desvinculacion = models.CharField(max_length=500, choices=(("Terminó tratamiento", "Terminó tratamiento"), ("Cambio de terapeuta", "Cambio de terapeuta"), ("Otro", "Otro")))


class Cita(models.Model):
    terapeuta = models.ForeignKey(Terapeuta, on_delete=models.CASCADE, null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    sala = models.CharField(max_length=50)
    detalle = models.CharField(max_length=100)
    def __str__(self):
        terapeuta_nombre = f"{self.terapeuta.user.first_name} {self.terapeuta.user.last_name}" if self.terapeuta else "Sin terapeuta"
        paciente_nombre = f"{self.paciente.user.first_name} {self.paciente.user.last_name}" if self.paciente else "Sin paciente"
        return f"{terapeuta_nombre} - {paciente_nombre}"

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

    


class Rutina(models.Model):
    terapeuta = models.ForeignKey(Terapeuta, on_delete=models.CASCADE, null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    estado = models.CharField(max_length=50, default="Pendiente", choices=(("Pendiente", "Pendiente"), ("Realizada", "Realizada"), ("Cancelada", "Cancelada")))
    angulo_inicial = models.IntegerField()
    angulo_final = models.IntegerField()
    repeticiones = models.IntegerField()
    velocidad = models.IntegerField()
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        terapeuta_nombre = f"{self.terapeuta.user.first_name} {self.terapeuta.user.last_name}" if self.terapeuta else "Sin terapeuta"
        paciente_nombre = f"{self.paciente.user.first_name} {self.paciente.user.last_name}" if self.paciente else "Sin paciente"
        return f"{terapeuta_nombre} - {paciente_nombre}"

class Sesion(models.Model):
    rutina = models.ForeignKey(Rutina, related_name='sesiones', on_delete=models.CASCADE, null=True, blank=True)
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()
    fecha = models.DateField()
    duracion = models.IntegerField()
    corriente = models.DecimalField(max_digits=5, decimal_places=2)
    observaciones = models.CharField(max_length=500)

    def __str__(self):
        terapeuta_nombre = f"{self.rutina.terapeuta.user.first_name} {self.rutina.terapeuta.user.last_name}" if self.rutina and self.rutina.terapeuta else "Sin terapeuta"
        paciente_nombre = f"{self.rutina.paciente.user.first_name} {self.rutina.paciente.user.last_name}" if self.rutina and self.rutina.paciente else "Sin paciente"
        return f"{terapeuta_nombre} - {paciente_nombre}"

class Horario(models.Model):
    terapeuta = models.ForeignKey(Terapeuta, on_delete=models.CASCADE, null=True, blank=True)
    dia = models.CharField(max_length=50, choices=(("Lunes", "Lunes"), ("Martes", "Martes"), ("Miércoles", "Miércoles"), ("Jueves", "Jueves"), ("Viernes", "Viernes"), ("Sábado", "Sábado"), ("Domingo", "Domingo")))
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()

    def __str__(self):
        return f"{self.terapeuta.user.first_name} {self.terapeuta.user.last_name} - {self.dia}"
