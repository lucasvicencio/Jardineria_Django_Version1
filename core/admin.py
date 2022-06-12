from django.contrib import admin
from .models import Categoria, Producto, Marca, Contacto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio"]

#Registrar Categoria
admin.site.register(Categoria)

#Registrar Marca
admin.site.register(Marca)

#Registrar Producto
admin.site.register(Producto, ProductoAdmin)

#Registrar Contacto
admin.site.register(Contacto)