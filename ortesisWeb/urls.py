
from django.contrib import admin
from django.urls import path
from ortesisWeb.views import *
from ortesisWeb.views import calendar_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', login_view, name='login'),
    path('calendar/', calendar_view, name='calendar'),
]
