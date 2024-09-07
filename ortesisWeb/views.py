from django.shortcuts import render

def calendar_view(request):
    # Lógica para el calendario
    return render(request, 'calendar.html')

def calendar_view2(request):
    # Lógica para el calendario
    return render(request, 'Calendario2.html')

def base_view(request):
    # Lógica para el calendario
    return render(request, 'base.html')

def perfil_view(request):
    return render(request, 'perfil.html')

def pacientes_view(request):
    return render(request, 'paciente.html')

def agenda_view(request):
    return render(request, 'agenda.html')