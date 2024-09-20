from django.shortcuts import render, redirect
from autenticacion.decorators import role_required
from .models import citas, Terapeuta
from django.http import HttpResponse
from django.core.paginator import Paginator

@role_required('Terapeuta')
def agenda(request):
    return render(request, 'agenda.html')

def perfil_view(request):
    return render(request, 'perfil.html')

def pacientes_view(request):
    return render(request, 'paciente_terapeuta.html')

def agendar_cita(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        fecha = request.POST['fecha']
        hora = request.POST['hora']
        sala = request.POST['sala']
        detalle = request.POST['detalle']
    
        terapeuta = Terapeuta.objects.get(id=1)
        
        cita = citas(
            id_terapeuta = terapeuta,
            titulo = titulo,
            fecha = fecha,
            hora = hora,
            sala = sala,
            detalle = detalle
        )
        cita.save()
        
        return redirect('agenda')
    return render(request, 'agenda.html')
