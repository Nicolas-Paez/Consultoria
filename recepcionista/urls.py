from django.urls import path
from . import views

urlpatterns = [
    path('terapeutas/', views.listar_terapeutas_activos, name='listar_terapeutas_activos'),
]
