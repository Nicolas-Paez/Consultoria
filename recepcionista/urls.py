from django.urls import path
from . import views

urlpatterns = [
    path('recepcionista_pacientes_activos', views.recepcionista_pacientes_activos, name='recepcionista_pacientes_activos'),
    path('recepcionista_terapeutas_activos/', views.recepcionista_terapeutas_activos, name='recepcionista_terapeutas_activos'),
    path('agregar_paciente', views.agregar_paciente, name='agregar_paciente')
]