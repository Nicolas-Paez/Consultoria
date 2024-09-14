from django.contrib.auth.models import User, Group
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, unique=True)  # RUT del usuario
    # El usuario puede tener múltiples roles
    roles = models.ManyToManyField(Group, related_name="user_roles")
    
    def __str__(self):
        return f'{self.user.username} ({self.rut})'