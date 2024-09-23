from django.urls import path
from . import views

urlpatterns = [
    path('administrador/gestion_terapeutas/', views.gestion_terapeutas, name='gestion_terapeutas'),
    path('base_admin/', views.base_admin_view, name='base_admin'),
    path('admin_pacientes/', views.admin_pacientes, name='admin_pacientes'),
    path('admin_recepcionistas/', views.admin_recepcionistas, name='admin_recepcionistas'),
    path('admin_terapeutas/',views.admin_terapeutas, name='admin_terapeutas'),
    path('logout/', views.logout_view, name='logout'),  # Para cerrar sesión
    path('agregar/', views.agregar_paciente_admin, name='agregar_paciente_admin'),
    path('administrador/agregar_terapeuta/', views.agregar_terapeuta, name='agregar_terapeuta'),
    path('api/provincias/', views.provincias_api, name='provincias_api'),
    path('api/comunas/', views.comunas_api, name='comunas_api'),
]