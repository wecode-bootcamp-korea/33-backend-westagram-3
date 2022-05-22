from django.urls import path
from health_check.views import ping

urlpatterns = [
	path("ping", ping)
]