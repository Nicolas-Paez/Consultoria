from django.shortcuts import render
from terapeuta.models import Terapeuta
from autenticacion.decorators import role_required

@role_required('Recepcionista')
def recepcionista_terapeutas_activos(request):
    '''query = request.GET.get('q', '')
    if query:
        terapeuta = Terapeuta.objects.filter(
            estado='activo',
            nombre__icontains=query
        ) | Terapeuta.objects.filter(
            estado='activo',
            rut__icontains=query
        )
    else:
    '''
    terapeuta = Terapeuta.objects.all()

    return render(request, 'recepcionista_terapeutas_activos.html', {'terapeuta': terapeuta})

@role_required('Recepcionista')
def recepcionista_pacientes_activos(request):
    return render(request, 'recepcionista_pacientes_activos.html')

@role_required('Recepcionista')
def agregar_paciente(request):
    return render(request, 'agregar_paciente.html')

@role_required('Recepcionista')
def asignar_terapeuta(request):
    terapeuta = Terapeuta.objects.all()
    return render(request, 'asignar_terapeuta.html', {'terapeuta': terapeuta})


    
