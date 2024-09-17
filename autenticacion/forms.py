from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm

class RutLoginForm(forms.Form):
    rut = forms.CharField(max_length=12, label="RUT")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    remember_me = forms.BooleanField(required=False, label="Recordarme")

class SendMailForm(forms.Form):
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Ingresa tu correo electrónico',
            'class': 'input-password_reset'  # Aquí puedes añadir clases CSS
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')  # Obtener el correo del formulario
        # Verificar si existe un usuario con el correo ingresado
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No existe ningún usuario con este correo.")
        return email

class PasswordResetForm(forms.Form):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Nueva contraseña'}),
        label='',  # Eliminar el label ya que se reemplaza por el placeholder
        help_text='Ingrese una nueva contraseña',
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Confirmar contraseña'}),
        label='',  # Eliminar el label ya que se reemplaza por el placeholder
        help_text='Repita la nueva contraseña',
    )

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2