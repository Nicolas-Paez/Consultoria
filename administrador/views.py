from django.shortcuts import render, redirect
from django.db import transaction
from autenticacion.decorators import role_required
from .forms import CrearTerapeutaForm, HorarioFormSet
from autenticacion.models import Provincia, Comuna
from django.http import JsonResponse

# Create your views here.
@role_required('Administrador')
def gestion_terapeutas(request):
    return render(request, 'gestion_terapeutas.html')

@role_required('Administrador')
def agregar_terapeuta(request):
    if request.method == 'POST':
        terapeuta_form = CrearTerapeutaForm(request.POST)
        horario_formset = HorarioFormSet(request.POST)

        if terapeuta_form.is_valid() and horario_formset.is_valid():
            with transaction.atomic(): # Para que si algo falla, no se guarde nada, asegura que todas las operaciones se realicen correctamente
                terapeuta = terapeuta_form.save()
                horario_formset.instance = terapeuta # Asignamos el terapeuta a los horarios
                horario_formset.save()
            
            return redirect('gestion_terapeutas') # Redirigimos a la vista de gestión de terapeutas
        
    else:
        terapeuta_form = CrearTerapeutaForm()
        horario_formset = HorarioFormSet()
    
    return render(request, 'agregar_terapeuta.html', {
        'terapeuta_form': terapeuta_form,
        'horario_formset': horario_formset
    })

#### CARGA DE DATOS DE REGIONES, PROVINCIAS Y COMUNAS ####
def provincias_api(request):
    region_id = request.GET.get("region")
    if region_id:
        provincias = Provincia.objects.filter(region_id=region_id).values("id", "nombre")
        return JsonResponse(list(provincias), safe=False)
    else:
        return JsonResponse([], safe=False)
    
def comunas_api(request):
    provincia_id = request.GET.get("provincia")
    if provincia_id:
        comunas = Comuna.objects.filter(provincia_id=provincia_id).values("id", "nombre")
        return JsonResponse(list(comunas), safe=False)
    else:
        return JsonResponse([], safe=False)