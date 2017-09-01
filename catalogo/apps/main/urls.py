from django.conf.urls import url, include
from .views import (
  FabricanteListView,
  ModeloListView,
  ProductosListView,
  AnioListView,
  KitListView

)

urlpatterns = [
    url(r'^api/fabricantes/$', FabricanteListView.as_view(), name='fabricante'),
    url(r'^api/modelos/$', ModeloListView.as_view(), name='modelos'),
    url(r'^api/productos/$', ProductosListView.as_view(), name='productos'),
    url(r'^api/anios/$', AnioListView.as_view(), name='anios'),
    url(r'^api/kits/$', KitListView.as_view(), name='kits')
]