from django.urls import path, include
from health_check.views import ping

urlpatterns = [
	path("ping", ping),
    path("", include("user.urls"))


]