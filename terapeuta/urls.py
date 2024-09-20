from django.urls import path
from . import views

urlpatterns = [
    path('agenda/', views.agenda, name='agenda'),
    path('agendar_cita', views.agendar_cita, name='agendar_cita'),
    path('calendar_asignar_paciente', views.calendar_asignar_paciente, name='calendar_asignar_paciente')
]