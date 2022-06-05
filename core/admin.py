from django.contrib import admin
from .models import Categoria
from .models import Producto
from .models import Marca

# Register your models here.

#Registrar Categoria
admin.site.register(Categoria)

#Registrar Marca
admin.site.register(Marca)

#Registrar Producto
admin.site.register(Producto)
