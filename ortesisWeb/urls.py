
from django.contrib import admin
from django.urls import path, include
from ortesisWeb.views import *

urlpatterns = [
    path('base/', base_view, name='home'),
    path('', include('autenticacion.urls')),
    path('', include('terapeuta.urls')),
    path("admin/", admin.site.urls),
    path('perfil/', perfil_view, name='perfil'),
    path('pacientes/', pacientes_view, name='pacientes'),
]
