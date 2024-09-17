import re
from itertools import cycle
from django import forms
from .models import Profile

class RutLoginForm(forms.Form):
    rut = forms.CharField(max_length=12, label="RUT")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    remember_me = forms.BooleanField(required=False, label="Recordarme")

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')

        # Validación del formato
        if not re.match(r'^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$', rut):
            raise forms.ValidationError('El RUT debe estar en el formato XX.XXX.XXX-X.')

        # Se remueve el punto y el guión
        clean_rut = rut.replace(".", "").replace("-", "")

        # Se extrae la parte numérica y se verifica el dígito
        num_part = clean_rut[:-1]
        dv = clean_rut[-1].upper()

        # Validación del dígito verificador
        reversed_digits = map(int, reversed(num_part))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        verificador = (-s) % 11
        verificador = 'K' if verificador == 10 else str(verificador)

        # Validación del dígito verificador
        if dv != verificador:
            raise forms.ValidationError('El dígito verificador del RUT no es válido.')

        return rut