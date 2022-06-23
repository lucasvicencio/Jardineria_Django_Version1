from distutils.command.upload import upload
from re import M
from tabnanny import verbose
from django.db import models

# Create your models here.

# Modelo para CATEGORIA

class Categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria

# Modelo para MARCA

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Modelo para PRODUCTO

class Producto(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id de Producto')
    nombre = models.CharField(max_length=50, verbose_name='Nombre del Producto')
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="productos", null=True)
    def __str__(self):
        return self.nombre


opciones_consultas = [
    [0, "Consultas"],
    [1, "Reclamo"],
    [2,"Sugerencia"],
    [3,"Felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
