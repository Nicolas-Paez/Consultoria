from django.urls import path
from . import views
from terapeuta.views import *

urlpatterns = [
    path('agenda/', views.agenda, name='agenda'),
    path('agendar_cita', views.agendar_cita, name='agendar_cita'),
    path('pacientes_terapeuta/', views.pacientes_view, name='paciente_terapeuta'),
    path('calendar', views.calendar, name= 'calendar'),
    path('paciente/cambiar-estado/<int:id>/', views.cambiar_estado_paciente, name='cambiar_estado_paciente'),
]