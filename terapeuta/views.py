from django.shortcuts import render
from autenticacion.decorators import role_required

@role_required('Terapeuta')
def agenda(request):
    return render(request, 'agenda.html')

def perfil_view(request):
    return render(request, 'perfil.html')

def pacientes_view(request):
    return render(request, 'paciente.html')
