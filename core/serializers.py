from .models import Producto
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True, min_length=3)
    

    def validate_nombre(self, value):
        existe = Producto.objects.filter(nombre__iexact=value).exists()

        if existe:
            raise serializers.ValidationError("Este Producto ya existe")

        return value
    
    
    class Meta:
        model = Producto
        fields = '__all__'