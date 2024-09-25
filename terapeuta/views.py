from django.shortcuts import render, redirect
from autenticacion.decorators import role_required
from .models import Cita, Terapeuta, Paciente
from django.http import HttpResponse
from django.core.paginator import Paginator
from datetime import date


@role_required('Terapeuta')
def agenda(request):
    paciente = Paciente.objects.all()
    return render(request, 'agenda.html', {'paciente':paciente})

def perfil_view(request):
    return render(request, 'perfil.html')

def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    return hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

def pacientes_view(request):
    pacientes_list = Paciente.objects.all()

    for paciente in pacientes_list:
        paciente.edad = calcular_edad(paciente.fecha_nacimiento)

    total_pacientes = pacientes_list.count() # Cuenta la cantidad de pacientes

    # Implementar la paginación
    paginator = Paginator(pacientes_list, 5)  # Muestra 5 pacientes por página
    page_number = request.GET.get('page')  # Obtiene el número de la página de la URL
    pacientes = paginator.get_page(page_number)  # Obtiene los pacientes de la página actual

    return render(request, 'paciente_terapeuta.html', {'pacientes': pacientes, 'total_pacientes': total_pacientes})

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

