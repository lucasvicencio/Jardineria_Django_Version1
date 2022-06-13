from django.contrib import admin
from .models import Categoria, Producto, Marca, Contacto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
   #list_filter = ["marca"]
    list_per_page = 5
    
#Registrar Categoria
admin.site.register(Categoria)

#Registrar Marca
admin.site.register(Marca)

#Registrar Producto
admin.site.register(Producto, ProductoAdmin)

#Registrar Contacto
admin.site.register(Contacto)