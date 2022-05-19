from django.urls import path 
from bada.views import MenuView 
# from health_check.views import ping
import json


urlpatterns = [
    path("", MenuView.as_view())
]

# a = json.loads("ss")
