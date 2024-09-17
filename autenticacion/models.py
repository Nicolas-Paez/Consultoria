from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=10, unique=True)  # RUT del usuario
    
    def __str__(self):
        return f'{self.user.username} ({self.rut})'
