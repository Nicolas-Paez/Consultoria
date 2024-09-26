from django.shortcuts import render
from terapeuta.models import Paciente

'''def calendar_view(request):
    # Lógica para el calendario
    paciente = Paciente.objects.all()
    return render(request, 'calendar.html', {'paciente': paciente})'''

def calendar_view2(request):
    # Lógica para el calendario
    return render(request, 'Calendario2.html')

def base_terapeuta_view(request):
    # Lógica para el calendario
    return render(request, 'base_terapeuta.html')

def perfil_view(request):
    return render(request, 'perfil.html')

def pacientes_view(request):
    return render(request, 'paciente.html')

def agenda_view(request):
    return render(request, 'agenda.html')

#RECEPCIONISTA

def base_recepcionista_view(request):
    return render(request, "base_recepcionista.html")

def terapeutas_view(request):
    return render(request, "terapeutas.html")