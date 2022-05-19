#from django.contrib import admin
from django.urls import path, include
from health_check.views import ping

urlpatterns = [
    path("menu", include("bada.urls"))
]
