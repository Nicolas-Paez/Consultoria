from django.shortcuts import render
from terapeuta.models import Terapeuta
from autenticacion.decorators import role_required

@role_required('Recepcionista')
def listar_terapeutas_activos(request):
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

    return render(request, 'terapeutas.html', {'terapeuta': terapeuta})
