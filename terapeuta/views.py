from django.shortcuts import render, redirect
from autenticacion.decorators import role_required
from .models import Cita, Terapeuta, Paciente
from django.http import HttpResponse
from django.http import JsonResponse

@role_required('Terapeuta')
def agenda(request):
    paciente = Paciente.objects.all()
    return render(request, 'agenda.html', {'paciente':paciente})

@role_required('Terapeuta')
def perfil_view(request):
    return render(request, 'perfil.html')

@role_required('Terapeuta')
def pacientes_view(request):
    pacientes = Paciente.objects.all() 
    return render(request, 'paciente.html', {'pacientes': pacientes})

@role_required('Terapeuta')
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

@role_required('Terapeuta')
def agendar_cita(request):    
    if request.user.is_authenticated:
        user_id = request.user.id
        terapeuta = Terapeuta.objects.get(user_id=user_id)
        terapeuta_id = terapeuta.id
        print(terapeuta_id)
        if request.method == 'POST':
            titulo = request.POST['titulo']
            paciente_id = request.POST['paciente']
            fecha = request.POST['fecha']
            hora = request.POST['hora']
            sala = request.POST['sala']
            detalle = request.POST['detalle']
        
            terapeuta_instance = Terapeuta.objects.get(id=terapeuta_id)
            
            paciente_instance = Paciente.objects.get(id=paciente_id)
            
            cita = Cita(
                terapeuta = terapeuta_instance,
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

