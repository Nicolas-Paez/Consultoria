from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Profile

# Registrar el modelo Profile en el panel de administración
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'rut')
    search_fields = ('user__username', 'rut')

# Llamar a la función para crear los grupos
def create_groups():
    Group.objects.get_or_create(name='Administrador')
    Group.objects.get_or_create(name='Terapeuta')
    Group.objects.get_or_create(name='Recepcionista')

# Ejecutar la creación de grupos cuando se inicie el servidor
create_groups()