from django.urls import path
from . import views

urlpatterns = [
    path('agenda/', views.agenda, name='agenda'),
    path('agendar_cita', views.agendar_cita, name='agendar_cita'),
    path('calendar', views.calendar, name= 'calendar'),
    path('pacientes/', views.pacientes_view, name='pacientes'),
    path('paciente/cambiar-estado/<int:id>/', views.cambiar_estado_paciente, name='cambiar_estado_paciente'),
]