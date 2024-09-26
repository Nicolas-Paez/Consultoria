from django.shortcuts import render, redirect
from autenticacion.decorators import role_required
from .models import Cita, Terapeuta, Paciente
from django.http import HttpResponse
from django.http import JsonResponse

@role_required('Terapeuta')

def agenda(request):
    # Obtener todas las citas y extraer las fechas
    citas = Cita.objects.all()
    fechas_citas = [cita.fecha for cita in citas]
    
    contexto = {
        'paciente': Paciente.objects.all(),
        'fechas_citas': fechas_citas,  # Agregar fechas de citas al contexto
    }
    
    return render(request, 'agenda.html', contexto)


def obtener_fechas_citas(request):
    citas = Cita.objects.values_list('fecha', flat=True)  # Solo obtenemos la fecha de las citas
    fechas_citas = list(citas)  # Convertimos a una lista para que sea serializable en JSON
    return JsonResponse({'fechas_citas': fechas_citas})



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

