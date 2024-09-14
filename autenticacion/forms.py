from django import forms

class RutLoginForm(forms.Form):
    rut = forms.CharField(max_length=12, label="RUT")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")