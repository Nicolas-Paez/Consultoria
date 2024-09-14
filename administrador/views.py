from django.shortcuts import render
from autenticacion.decorators import role_required

# Create your views here.
@role_required('Administrador')
def gestion_terapeutas(request):
    return render(request, 'gestion_terapeutas.html')