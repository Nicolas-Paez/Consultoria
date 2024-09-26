
from django.contrib import admin
from django.urls import path, include
from ortesisWeb.views import *

urlpatterns = [
    path('base_terapeuta/', base_terapeuta_view, name='home'),
    path('base_recepcionista/', base_recepcionista_view, name='base_recepcionista'),
    path('', include('autenticacion.urls')),
    path('', include('administrador.urls')),
    path('', include('terapeuta.urls')),
    path('', include('recepcionista.urls')),
    path("admin/", admin.site.urls),
    path('perfil/', perfil_view, name='perfil'),
    path('pacientes/', pacientes_view, name='pacientes'),
    path('recepcionista/', include('recepcionista.urls')),
    path('terapeutas', terapeutas_view, name='terapeutas'),
]
