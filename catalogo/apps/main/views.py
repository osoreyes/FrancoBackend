from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import filters
from . models import *
from .serializers import (
  FabricanteSerializer,
  ModeloSerializer,
  AnioSerializer,
  DetalleProductoSerializer,
  KitSerializer
)

class FabricanteListView(ListAPIView):
  queryset = Fabricante.objects.all()
  serializer_class = FabricanteSerializer

class AnioListView(ListAPIView):
  queryset = Anio.objects.all().order_by('-anio')
  serializer_class = AnioSerializer

class ModeloListView(ListAPIView):

  queryset = Modelo.objects.all()
  serializer_class = ModeloSerializer
  filter_backends = (filters.DjangoFilterBackend,)
  filter_fields = ('fabricante',)

class ProductosListView(ListAPIView):

  serializer_class = DetalleProductoSerializer

  def get_queryset(self):
    if self.request.query_params.get('anio', None):
      anio = int(self.request.query_params.get('anio', None))
      productos = DetalleProducto.objects.filter(anio_inicio__anio__lte=anio,anio_fin__anio__gte=anio)
      return productos
    if self.request.query_params.get('codigo', None):
      codigo = str(self.request.query_params.get('codigo', None))
      productos = DetalleProducto.objects.filter(producto__codigo__contains=codigo)
      return productos
    return DetalleProducto.objects.all()

class KitListView(ListAPIView):

  serializer_class = KitSerializer

  def get_queryset(self):
    if self.request.query_params.get('id', None):
      id = int(self.request.query_params.get('id', None))
      productos = KitProducto.objects.filter(productos__id=id)
      return productos
    return KitProducto.objects.all()