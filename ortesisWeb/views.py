from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def calendar_view(request):
    # Lógica para el calendario
    return render(request, 'calendar.html')