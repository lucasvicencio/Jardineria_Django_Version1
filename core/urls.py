from cgitb import html
from unicodedata import name
from django.urls import path
from .views import home, Donativos, formularioContacto, listar_productos, metodoPago, registrar, contacto, agregar_producto, flash, listar_productos


urlpatterns = [
    path('', home,name='home.html'),
    path('formularioContacto.html', formularioContacto,name="formularioContacto.html"),
    path('Donativos.html', Donativos, name="Donativos.html"),
    path('metodoPago.html', metodoPago, name="metodoPago.html"),
    path('registrar.html', registrar, name="registrar.html"),
    path('contacto.html', contacto, name="contacto.html"),
    path('agregar-producto.html', agregar_producto, name='agregar_producto'),
    path('flash.html', flash, name="flash.html"),
    path('listar-productos', listar_productos, name="listar_productos")
]

