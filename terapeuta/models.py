from django.db import models
from django.contrib.auth.models import User

class Terapeuta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    especialidad = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    titulo = models.CharField(max_length=100)
    experiencia = models.IntegerField(max_length=2)
    presentacion = models.CharField(max_length=500)
    correo_contacto = models.EmailField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    terapeuta = models.ForeignKey(Terapeuta, on_delete=models.CASCADE)
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

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Citas(models.Model):
    terapeuta = models.ForeignKey(Terapeuta, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    sala = models.CharField(max_length=50)
    detalle = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.terapeuta.user.first_name} {self.terapeuta.user.last_name} - {self.paciente.user.first_name} {self.paciente.user.last_name}"

class Rutina(models.Model):
    terapeuta = models.ForeignKey(Terapeuta, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    estado = models.CharField(max_length=50, default="Pendiente", choices=(("Pendiente", "Pendiente"), ("Realizada", "Realizada"), ("Cancelada", "Cancelada")))
    angulo_inicial = models.IntegerField()
    angulo_final = models.IntegerField()
    repeticiones = models.IntegerField()
    velocidad = models.IntegerField()
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.terapeuta.user.first_name} {self.terapeuta.user.last_name} - {self.paciente.user.first_name} {self.paciente.user.last_name}"

class Sesion(models.Model):
    rutina = models.ForeignKey(Rutina, related_name='sesiones', on_delete=models.CASCADE)
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()
    fecha = models.DateField()
    duracion = models.IntegerField()
    corriente = models.DecimalField(max_digits=5, decimal_places=2)
    observaciones = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.terapeuta.user.first_name} {self.terapeuta.user.last_name} - {self.paciente.user.first_name} {self.paciente.user.last_name}"