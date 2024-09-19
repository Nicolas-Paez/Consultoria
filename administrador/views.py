from django.shortcuts import redirect, render
from autenticacion.decorators import role_required

# Create your views here.
@role_required('Administrador')
def gestion_terapeutas(request):
    return render(request, 'admin_terapeutas.html')
def base_admin_view(request):
    return render(request, 'base_admin.html')

def admin_pacientes(request):
    # Lógica para listar o gestionar pacientes desde la vista del administrador
    return render(request, 'admin_pacientes.html')

def admin_recepcionistas(request):
    # Lógica para listar o gestionar recepcionistas desde la vista del administrador
    return render(request, 'admin_recepcionistas.html')
def admin_terapeutas(request):
    return render (request,'admin_terapeutas.html')

def agregar_paciente_admin(request):
    # lógica de la vista
    return render(request, 'agregar_paciente_admin.html')

def logout_view(request):
    # Lógica para cerrar la sesión
    # Puedes usar Django's auth logout
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')  # Redirigir al login después de cerrar sesión
