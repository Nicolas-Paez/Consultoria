from django.shortcuts import render, redirect
from autenticacion.decorators import role_required
from .models import Cita, Terapeuta, Paciente
from django.http import HttpResponse

@role_required('Terapeuta')
def agenda(request):
    paciente = Paciente.objects.all()
    return render(request, 'agenda.html', {'paciente':paciente})

def perfil_view(request):
    return render(request, 'perfil.html')

def pacientes_view(request):
    return render(request, 'paciente.html')

def agendar_cita(request):
    pacientes = Paciente.objects.all()
    if request.method == 'POST':
        titulo = request.POST['titulo']
        paciente_id = request.POST['paciente']
        fecha = request.POST['fecha']
        hora = request.POST['hora']
        sala = request.POST['sala']
        detalle = request.POST['detalle']
    
        terapeuta = Terapeuta.objects.get(id=1)
        
        paciente_instance = Paciente.objects.get(id=paciente_id)
        
        cita = Cita(
            terapeuta = terapeuta,
            titulo = titulo,
            paciente = paciente_instance,
            fecha = fecha,
            hora = hora,
            sala = sala,
            detalle = detalle
        )
        cita.save()
        
        return redirect('agenda')
    return render(request, 'agenda.html', {'pacientes':pacientes})

def calendar(request):
    paciente = Paciente.objects.all()
    print(paciente)
    return render (request, 'calendar.html', {'paciente':paciente})

