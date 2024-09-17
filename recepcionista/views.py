from django.shortcuts import render
from terapeuta.models import Terapeuta
from autenticacion.decorators import role_required

@role_required('Recepcionista')
def recepcionista_terapeutas_activos(request):
    query = request.GET.get('q', '')
    if query:
        terapeuta = Terapeuta.objects.filter(
            estado='Activo',
            nombre__icontains=query
        ) | Terapeuta.objects.filter(
            estado='Activo',
            rut__icontains=query
        )
    else:
        terapeuta = Terapeuta.objects.filter(estado='Activo')

    return render(request, 'recepcionista_terapeutas_activos.html', {'terapeuta': terapeuta})

@role_required('Recepcionista')
def recepcionista_pacientes_activos(request):
    return render(request, 'recepcionista_pacientes_activos.html')
    
