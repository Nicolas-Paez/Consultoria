from django.shortcuts import render

# Create your views here.
def gestion_terapeutas(request):
    return render(request, 'gestion_terapeutas.html')