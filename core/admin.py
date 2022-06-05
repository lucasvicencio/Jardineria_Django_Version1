from django.contrib import admin
from .models import Categoria
from .models import Producto

# Register your models here.

#Registrar Categoria
admin.site.register(Categoria)



#Registrar Producto
admin.site.register(Producto)
