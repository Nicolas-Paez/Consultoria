from django.shortcuts import render

def agenda(request):
    return render(request, 'agenda.html')

def perfil_view(request):
    return render(request, 'perfil.html')

def pacientes_view(request):
    return render(request, 'paciente.html')
