from django.urls import path
from . import views
from .views import Login, Redireccionamiento  # Importa las clases correctas
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('redireccionamiento/', Redireccionamiento.as_view(), name='redireccionamiento'),
    path('', views.login, name='home'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]