from django import forms
from django.contrib.auth.models import User, Group
from autenticacion.models import Profile
from terapeuta.models import Terapeuta, Horario
from autenticacion.models import Region, Provincia, Comuna  # Asegúrate de importar tus modelos
from django.forms import inlineformset_factory

class CrearTerapeutaForm(forms.ModelForm):
    # Campo del modelo 'Profile'

    rut = forms.CharField(
        max_length=12,
        label='Rut', 
        required=True,
        widget=forms.TextInput(attrs={'class':'campo-formulario','placeholder': 'Ej: XX.XXX.XXX-X'})
    )

    # Campos del modelo 'User'

    first_name = forms.CharField(
        max_length=150, 
        label='Nombres', 
        required=True,
        widget=forms.TextInput(attrs={'class':'campo-formulario','placeholder': 'Ej: Juan Alberto'})
    )
    last_name = forms.CharField(
        max_length=150, 
        label='Apellidos', 
        required=True,
        widget=forms.TextInput(attrs={'class':'campo-formulario','placeholder': 'Ej: Pérez González'})
    )
    email = forms.EmailField(
        label='Correo electrónico', 
        required=True,
        widget=forms.EmailInput(attrs={'class':'campo-formulario','placeholder': 'correoejemplo@ejemplos.com'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'campo-formulario','placeholder': 'Contraseña'}), 
        label='Contraseña', 
        required=True
    )

    # Campos del modelo 'Profile'

    telefono = forms.CharField(
        max_length=12, 
        label='Teléfono', 
        required=True,
        widget=forms.TextInput(attrs={'class':'campo-formulario','placeholder': 'Ej: +56 9 1234 5678'})
    )
    fecha_nacimiento = forms.DateField(
        label='Fecha de nacimiento', 
        required=True,
        widget=forms.DateInput(attrs={'class':'campo-formulario', 'type': 'date'})
    )
    direccion = forms.CharField(
        max_length=255, 
        label='Dirección', 
        required=True,
        widget=forms.TextInput(attrs={'class':'campo-formulario','placeholder': 'Ej: Calle Ejemplo 123'})
    )
    region = forms.ModelChoiceField(
        queryset=Region.objects.all(), 
        label='Región', 
        required=True,
        widget=forms.Select(attrs={'class':'campo-formulario'})
    )
    provincia = forms.ModelChoiceField(
        queryset=Provincia.objects.none(), 
        label='Provincia', 
        required=True,
        widget=forms.Select(attrs={'class':'campo-formulario'})
    )
    comuna = forms.ModelChoiceField(
        queryset=Comuna.objects.none(), 
        label='Comuna', 
        required=True,
        widget=forms.Select(attrs={'class':'campo-formulario'})
    )
    sexo = forms.ChoiceField(
        choices=(('M', 'Masculino'), ('F', 'Femenino')), 
        label='Sexo', 
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    # Campos del modelo 'Terapeuta'
    especialidad = forms.CharField(
        max_length=100, 
        label='Especialidad', 
        required=True,
        widget=forms.TextInput(attrs={'class':'campo-formulario', 'placeholder' :'Ej: Articulaciones Superiores'})
    )
    fecha_contratacion = forms.DateField(
        label='Fecha de contratación', 
        required=True,
        widget=forms.DateInput(attrs={'class':'campo-formulario', 'type': 'date'})
    )
    titulo = forms.CharField(
        max_length=100, 
        label='Título', 
        required=True,
        widget=forms.TextInput(attrs={'class':'campo-formulario', 'placeholder': 'Ej: Licenciado en Terapia Ocupacional'})
    )
    experiencia = forms.IntegerField(
        label='Experiencia', 
        required=True,
        widget=forms.NumberInput(attrs={'class':'campo-formulario'})
    )
    presentacion = forms.CharField(
        max_length=500, 
        label='Presentación', 
        required=False,
        widget=forms.Textarea(attrs={'class':'campo-formulario','rows': 3})
    )
    correo_contacto = forms.EmailField(
        label='Correo de contacto', 
        required=False,
        widget=forms.EmailInput(attrs={'class':'campo-formulario','placeholder': 'correoejemplo@ejemplos.com'})
    )

    class Meta:
        model = Terapeuta
        fields = [
            'rut',
            'first_name',
            'last_name',
            'email',
            'password',
            'telefono',
            'fecha_nacimiento',
            'direccion',
            'region',
            'provincia',
            'comuna',
            'sexo',
            'especialidad',
            'fecha_contratacion',
            'titulo',
            'experiencia',
            'presentacion',
            'correo_contacto'
        ]

    def save(self, commit=True):
        # Creamos el usuario primero
        user = User.objects.create_user(
            username=self.cleaned_data['rut'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
        )
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            
        # Agregar el usuario al grupo 'Terapeuta'
        grupo_terapeuta, created = Group.objects.get_or_create(name='Terapeuta')
        user.groups.add(grupo_terapeuta)  # Añadimos el usuario al grupo
        
        # Creamos el perfil del usuario
        profile = Profile.objects.create(
            user=user,
            rut=self.cleaned_data['rut'],
            telefono=self.cleaned_data['telefono'],
            fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
            direccion=self.cleaned_data['direccion'],
            region=self.cleaned_data['region'],  # Ahora es una instancia de Region
            provincia=self.cleaned_data['provincia'],  # Ahora es una instancia de Provincia
            comuna=self.cleaned_data['comuna'],  # Ahora es una instancia de Comuna
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
        
        return terapeuta  # Retornamos el terapeuta creado
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'region' in self.data:
            try:
                self.fields['provincia'].queryset = Provincia.objects.filter(region_id=self.data['region'])
            except (ValueError, TypeError):
                pass  # Manejo de errores si la región no es válida
        elif self.instance.pk:
            self.fields['provincia'].queryset = self.instance.region.provincia_set.all()

        if 'provincia' in self.data:
            try:
                self.fields['comuna'].queryset = Comuna.objects.filter(provincia_id=self.data['provincia'])
            except (ValueError, TypeError):
                pass  # Manejo de errores si la provincia no es válida
        elif self.instance.pk:
            self.fields['comuna'].queryset = self.instance.provincia.comuna_set.all()

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['dia', 'hora_inicio', 'hora_final']
        widgets = {
            'dia': forms.Select(attrs={'class':'seleccion'}),
            'hora_inicio': forms.TimeInput(attrs={'class':'campo-formulario', 'type': 'time'}),
            'hora_final': forms.TimeInput(attrs={'class':'campo-formulario', 'type': 'time'}),
        }

# Creamos el formset para los horarios del terapeuta (inlineformset)
HorarioFormSet = inlineformset_factory(
    Terapeuta,
    Horario,
    form=HorarioForm,
    extra=7,  # 7 días de la semana, lunes a domingo
)
