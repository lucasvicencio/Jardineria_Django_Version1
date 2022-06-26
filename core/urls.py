from cgitb import html
from unicodedata import name
from django.urls import path, include
from .views import home, Donativos, formularioContacto, listar_productos, metodoPago, registrar, contacto, agregar_producto, flash, listar_productos, modificar_producto, eliminar_producto, registro, ProductoViewset, error_facebook
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)

#localhost:8000/api/producto

urlpatterns = [
    path('', home,name='home.html'),
    path('formularioContacto.html', formularioContacto,name="formularioContacto.html"),
    path('Donativos.html', Donativos, name="Donativos.html"),
    path('metodoPago.html', metodoPago, name="metodoPago.html"),
    path('registrar.html', registrar, name="registrar.html"),
    path('contacto.html', contacto, name="contacto.html"),
    path('agregar-producto.html', agregar_producto, name='agregar_producto'),
    path('flash.html', flash, name="flash.html"),
    path('listar-productos', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
    path('error-facebook/', error_facebook, name="error_facebook.html"),
]

