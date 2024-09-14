from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import RutLoginForm
from .models import Profile

def login(request):
    if request.method == 'POST':
        form = RutLoginForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            password = form.cleaned_data['password']
            user = authenticate(request, rut=rut, password=password)
            
            if user is not None:
                login(request, user)
                # Verificar roles del usuario
                roles = user.profile.roles.all()
                
                if roles.count() == 1:  # Si el usuario tiene un solo rol
                    return redireccionamiento_segun_rol(user, roles.first())
                elif roles.count() > 1:  # Si tiene múltiples roles, mostrar opciones
                    return render(request, 'elegir_rol.html', {'roles': roles})
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Credenciales incorrectas'})
    else:
        form = RutLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def elegir_rol(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        group = Group.objects.get(name=role)
        return redireccionamiento_segun_rol(request.user, group)
    
    return render(request, 'elegir_rol.html', {'roles': request.user.profile.roles.all()})

def redireccionamiento_segun_rol(user, role):
    """Redirige según el rol"""
    if role.name == 'Administrador':
        return redirect('gestion_terapeutas')
    elif role.name == 'Terapeuta':
        return redirect('agenda')
    elif role.name == 'Recepcionista':
        return redirect('listar_terapeutas_activos')
    return redirect('login')  # Redirige en caso de no encontrar un rol

def logout(request):
    logout(request)
    return redirect('login')