from django.db import models

class Fabricante(models.Model):
  """Model definition for Fabricante."""

  nombre = models.CharField(max_length=50)

  class Meta:
    """Meta definition for Fabricante."""

    verbose_name = 'Fabricante'
    verbose_name_plural = 'Fabricantes'

  def __str__(self):
    """Unicode representation of Fabricante."""
    return self.nombre

class Modelo(models.Model):
  """Model definition for Modelo."""

  nombre = models.CharField(max_length=50)
  fabricante = models.ForeignKey(Fabricante)

  class Meta:
    """Meta definition for Modelo."""

    verbose_name = 'Modelo'
    verbose_name_plural = 'Modelos'

  def __str__(self):
    """Unicode representation of Modelo."""
    return self.nombre

class Anio(models.Model):
  """Model definition for Anio."""

  anio = models.IntegerField()

  class Meta:
    """Meta definition for Anio."""

    verbose_name = 'Año'
    verbose_name_plural = 'Años'

  def __str__(self):
    """Unicode representation of Anio."""
    return '%s'%self.anio



class Producto(models.Model):
  """Model definition for Producto."""

  nombre = models.CharField(max_length=50)
  codigo = models.CharField(max_length=50)
  modelo = models.ForeignKey(Modelo, related_name='modelo')

  class Meta:
    """Meta definition for Producto."""

    verbose_name = 'Producto'
    verbose_name_plural = 'Productos'

  def __str__(self):
    """Unicode representation of Producto."""
    return self.nombre

class DetalleProducto(models.Model):
  """Model definition for DetalleProducto."""
  producto = models.ForeignKey(Producto, related_name='producto')
  activo = models.BooleanField(default=True)
  anio_inicio = models.ForeignKey(Anio, related_name='anio_inicio')
  anio_fin = models.ForeignKey(Anio, related_name='anio_fin')
  motor = models.CharField(max_length=50)
  imagen = models.ImageField(upload_to="productos/imagenes")

  class Meta:
    """Meta definition for DetalleProducto."""

    verbose_name = 'DetalleProducto'
    verbose_name_plural = 'Detalle Producto'

  def __str__(self):
    """Unicode representation of DetalleProducto."""
    return '%s %s'%(self.producto.nombre, self.motor)


class KitProducto(models.Model):
  """Model definition for KitProducto."""

  nombre = models.CharField(max_length=50)
  codigo = models.CharField(max_length=50)
  productos = models.ManyToManyField(Producto)
  imagen = models.ImageField(upload_to="kits/imagenes")

  class Meta:
    """Meta definition for KitProducto."""

    verbose_name = 'KitProducto'
    verbose_name_plural = 'Kit de Productos'

  def __str__(self):
    """Unicode representation of KitProducto."""
    return self.nombre
