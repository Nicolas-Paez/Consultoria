
from django.contrib import admin
from django.urls import path, include
from ortesisWeb.views import *

urlpatterns = [
    path('base/', base_view, name='home'),
    path('', include('autenticacion.urls')),
    path("admin/", admin.site.urls),
    path('calendar/', calendar_view, name='agenda/calendar'),
    path('calendar2/', calendar_view2, name='Calendario2'),
    path('base/', base_view, name='base'),
    path('perfil/', perfil_view, name='perfil'),
    path('pacientes/', pacientes_view, name='pacientes'),
    path('agenda/', agenda_view, name='agenda'),
]
