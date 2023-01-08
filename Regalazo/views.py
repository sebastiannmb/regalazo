from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Bienvenido a Regalazo")

def index(request):
    return render(request, 'index.html', context={})


