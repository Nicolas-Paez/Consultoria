
from django.contrib import admin
from django.urls import path
from ortesisWeb.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', login_view, name='login'),
    path('calendar/', calendar_view, name='agenda/calendar'),
    path('calendar2/', calendar_view2, name='Calendario2'),
    path('base/', base_view, name='base'),
]
