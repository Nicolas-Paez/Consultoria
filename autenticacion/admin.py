from django.contrib.auth.models import Group

# Creación de grupos
def create_groups():
    Group.objects.get_or_create(name='Administrador')
    Group.objects.get_or_create(name='Terapeuta')
    Group.objects.get_or_create(name='Recepcionista')