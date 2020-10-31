from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def ronan(request):
    return HttpResponse("Hello, Ronan!")

def brian(request):
    return HttpResponse("Hello, Brian!")