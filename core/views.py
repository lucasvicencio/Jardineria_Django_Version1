from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto
from .forms import ContactoForm, ProductoForm


# Create your views here.

def flash(request):
    productos = Producto.objects.all()
    data = {

        'productos': productos
    }
    return render(request, 'core/flash.html', data)

def home(request):

    return render(request, 'core/home.html')

def formularioContacto(request):

    return render(request, 'core/formularioContacto.html')

def Donativos(request):

    return render(request, 'core/Donativos.html')

def metodoPago(request):

    return render(request, 'core/metodoPago.html')
    
def registrar(request):
    return render(request, 'core/registrar.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto enviado"
        else:
            data["form"] = formulario

    return render(request, 'core/contacto.html', data)

def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'core/producto/agregar.html', data)

def flash(request):

    return render(request, 'core/flash.html')

def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }
    return render(request, 'core/producto/listar.html', data)