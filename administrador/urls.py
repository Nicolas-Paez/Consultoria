from django.urls import path
from . import views

urlpatterns = [
    path('administrador/gestion_terapeutas/', views.gestion_terapeutas, name='gestion_terapeutas'),
    path('administrador/agregar_terapeuta/', views.agregar_terapeuta, name='agregar_terapeuta'),
    path('api/provincias/', views.provincias_api, name='provincias_api'),
    path('api/comunas/', views.comunas_api, name='comunas_api'),
]