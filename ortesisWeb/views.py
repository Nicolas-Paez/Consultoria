from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def calendar_view(request):
    # Lógica para el calendario
    return render(request, 'calendar.html')

def calendar_view2(request):
    # Lógica para el calendario
    return render(request, 'Calendario2.html')

def base_view(request):
    # Lógica para el calendario
    return render(request, 'base.html')