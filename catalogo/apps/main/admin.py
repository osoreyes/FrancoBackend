from django.contrib import admin
from .models import *

admin.site.register(Fabricante)
admin.site.register(Producto)
admin.site.register(Modelo)
admin.site.register(Anio)
admin.site.register(KitProducto)
admin.site.register(DetalleProducto)