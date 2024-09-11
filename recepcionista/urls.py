from django.urls import path
from . import views

urlpatterns = [
    path('terapeuta/', views.listar_terapeutas_activos, name='listar_terapeutas_activos'),
]
