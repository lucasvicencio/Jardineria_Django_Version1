from unicodedata import name
from django.urls import path
from .views import Donativos, home, formularioContacto, metodoPago


urlpatterns = [
    path('', home,name='home.html'),
    path('formularioContacto.html', formularioContacto,name='formularioContacto.html'),
    path('Donativos.html', Donativos, name='Donativos.html'),
    path('metodoPago.html', metodoPago, name='metodoPago.html')

]