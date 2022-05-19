from django.urls import path 
from bada.views import ProductsView 
# from health_check.views import ping
import json


urlpatterns = [
    path("", ProductsView.as_view())
]

a = json.loads("ss")
