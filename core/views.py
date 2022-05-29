from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):

    return render(request, 'core/home.html')

def formularioContacto(request):

    return render(request, 'core/formularioContacto.html')

def Donativos(request):

    return render(request, 'core/Donativos.html')

def metodoPago(request):

    return render(request, 'core/metodoPago.html')
    