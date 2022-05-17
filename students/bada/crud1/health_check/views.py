from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def ping(request):

    print(f"client's request {request}")

    return HttpResponse('pong')