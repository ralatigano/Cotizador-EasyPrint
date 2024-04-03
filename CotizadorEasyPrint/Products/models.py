from django.db import models
from core.models import Presupuesto

# Create your models here.
class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    categoria = models.ForeignKey(on_delete=models.CASCADE, to='Products.Categoria', default=None,blank=True)
    ancho = models.FloatField(null=True, blank=True, default=0)
    alto = models.FloatField(null=True, blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    #--Atributos del modelo útiles para el armado de presupuestos pero no necesarias para la declaración de productos en si-----#
    cliente=models.CharField(max_length=200, null=True, blank=True, default=None)
    info_adic = models.CharField(max_length=200, null=True, blank=True, default=None)
    cantidad = models.IntegerField(null=True, blank=True, default=None)
    desc_plata = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True, default=0)
    desc_porcentaje = models.IntegerField(null=True, blank=True, default=0)
    resultado = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True, default=0)
    presupuesto = models.ForeignKey(on_delete=models.CASCADE, to='core.Presupuesto', default=None,blank=True, null=True)
    caso_part = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    class META():
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, blank=True, default=None, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
    class META():
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"