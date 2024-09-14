from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class RutAuthBackend(ModelBackend):
    def authenticate(self, request, rut=None, password=None, **kwargs):
        try:
            user = User.objects.get(profile__rut=rut)  # Busca el usuario por el RUT
            if user.check_password(password):  # Verifica la contraseña
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
