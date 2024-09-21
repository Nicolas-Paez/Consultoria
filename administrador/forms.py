from django import forms
from django.contrib.auth.models import User
from autenticacion.models import Profile
from terapeuta.models import Terapeuta, Horario
from django.forms import inlineformset_factory

class CrearTerapeutaForm(forms.ModelForm):
    
    # Campo del modelo 'Profile'
    rut = forms.CharField(max_length=12, label='Rut', required=True)
    # Campos del modelo 'User'
    first_name = forms.CharField(max_length=150, label='Nombres', required=True)
    last_name = forms.CharField(max_length=150, label='Apellidos', required=True)
    email = forms.EmailField(label='Correo electrónico', required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña', required=True)
    #Campos del modelo 'Profile'
    telefono = forms.CharField(max_length=12, label='Teléfono', required=True)
    fecha_nacimiento = forms.DateField(label='Fecha de nacimiento', required=True)
    direccion = forms.CharField(max_length=255, label='Dirección', required=True)
    region = forms.CharField(max_length=255, label='Región', required=True)
    provincia = forms.CharField(max_length=255, label='Provincia', required=True)
    comuna = forms.CharField(max_length=255, label='Comuna', required=True)
    sexo = forms.ChoiceField(choices=(('M', 'Masculino'), ('F', 'Femenino')), label='Sexo', required=True)
    # Campos del modelo 'Terapeuta'
    especialidad = forms.CharField(max_length=100, label='Especialidad', required=True)
    fecha_contratacion = forms.DateField(label='Fecha de contratación', required=True)
    titulo = forms.CharField(max_length=100, label='Título', required=True)
    experiencia = forms.IntegerField(label='Experiencia', required=True)
    presentacion = forms.CharField(max_length=500, label='Presentación', required=False)
    correo_contacto = forms.EmailField(label='Correo de contacto', required=False)

    class Meta:
        model = Terapeuta
        fields = ['rut', 'first_name', 'last_name', 'email', 'password', 'telefono', 'fecha_nacimiento', 'direccion', 'region', 'provincia', 'comuna', 'sexo', 'especialidad', 'fecha_contratacion', 'titulo', 'experiencia', 'presentacion', 'correo_contacto']

    def save(self, commit=True):
        # Creamos el usuario primero
        user = User.objects.create_user(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
        )
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        
        # Creamos el perfil del usuario
        profile = Profile.objects.create(
            user=user,
            rut=self.cleaned_data['rut'],
            telefono=self.cleaned_data['telefono'],
            fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
            direccion=self.cleaned_data['direccion'],
            region=self.cleaned_data['region'],
            provincia=self.cleaned_data['provincia'],
            comuna=self.cleaned_data['comuna'],
            sexo=self.cleaned_data['sexo']
        )
        if commit:
            profile.save()
        
        # Creamos el terapeuta
        terapeuta = Terapeuta.objects.create(
            user=user,
            especialidad=self.cleaned_data['especialidad'],
            fecha_contratacion=self.cleaned_data['fecha_contratacion'],
            titulo=self.cleaned_data['titulo'],
            experiencia=self.cleaned_data['experiencia'],
            presentacion=self.cleaned_data['presentacion'],
            correo_contacto=self.cleaned_data['correo_contacto']
        )
        if commit:
            terapeuta.save()
        
        return terapeuta    # Retornamos el terapeuta creado

# Creamos el formset para los horarios del terapeuta (inlineformset)

HorarioFormSet = inlineformset_factory(
    Terapeuta,
    Horario,
    fields=('dia', 'hora_inicio', 'hora_final'),
    extra=7, # 7 días de la semana, lunes a domingo, de esta forma se crean 7 formularios para los horarios
)