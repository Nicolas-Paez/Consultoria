from django.shortcuts import render, redirect
from autenticacion.decorators import role_required
from .models import Cita, Terapeuta, Paciente
from django.http import HttpResponse
from django.http import JsonResponse

@role_required('Terapeuta')
def agenda(request):
    paciente = Paciente.objects.all()
    return render(request, 'agenda.html', {'paciente':paciente})

def perfil_view(request):
    return render(request, 'perfil.html')

def pacientes_view(request):
    pacientes = Paciente.objects.all() 
    return render(request, 'paciente.html', {'pacientes': pacientes})

def cambiar_estado_paciente(request, id):
    if request.method == "POST":
        try:
            paciente = Paciente.objects.get(id=id)
            paciente.is_active = False 
            paciente.save()
            return JsonResponse({"status": "success", "message": "CAMBIO DE ESTADO EXITOSO"})
        except Paciente.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Paciente no encontrado"}, status=404)
    return JsonResponse({"status": "error", "message": "Método no permitido"}, status=405)

def agendar_cita(request):
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
    return render(request, 'agenda.html')

def calendar(request):
    paciente = Paciente.objects.all()
    print(paciente)
    return render (request, 'calendar.html', {'paciente':paciente})

