from .models import *
from rest_framework import routers, serializers, viewsets, generics
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.serializers import ModelSerializer

class FabricanteSerializer(ModelSerializer):
  class Meta:
    model = Fabricante
    fields = ('id', 'nombre',)

class ModeloSerializer(serializers.HyperlinkedModelSerializer):
  fabricante = FabricanteSerializer()
  
  class Meta:
    model = Modelo
    fields = ('id', 'nombre', 'fabricante')

class AnioSerializer(serializers.HyperlinkedModelSerializer):
  
  class Meta:
    model = Anio
    fields = ('anio',)

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
  modelo = ModeloSerializer()
  
  class Meta:
    model = Producto
    fields = ('id', 'nombre', 'codigo', 'modelo')

class DetalleProductoSerializer(serializers.HyperlinkedModelSerializer):
  producto = ProductoSerializer()
  anio_inicio = AnioSerializer()
  anio_fin = AnioSerializer()
  
  class Meta:
    model = DetalleProducto
    fields = ('id', 'producto', 'anio_inicio', 'anio_fin', 'motor', 'imagen')

class KitSerializer(serializers.HyperlinkedModelSerializer):
  productos = ProductoSerializer(read_only=True, many=True)
  
  class Meta:
    model = KitProducto
    fields = ('id', 'nombre', 'codigo', 'productos', 'imagen')