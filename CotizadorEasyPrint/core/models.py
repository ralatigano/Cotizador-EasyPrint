from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Presupuesto(models.Model):
    numero=models.IntegerField(primary_key=True)
    desc_plata = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    seña=models.FloatField(null=True,blank=True)
    saldo=models.FloatField(null=True,blank=True)
    cliente=models.ForeignKey(on_delete=models.CASCADE, to='core.Cliente', default=None,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return str(self.numero)
    class META():
        ordering = ["-created"]
        verbose_name = "Presupuesto"
        verbose_name_plural = "Presupuestos"

estado_pedido = [ ('Sin seña','Sin seña'), ('Señado', 'Señado'), ('En proceso','En proceso'), ('Para retirar', 'Para retirar'), ('Entregado','Entregado'), ('Pagado', 'Pagado'), ('Cancelado','Cancelado')]
class Pedido(models.Model):
    numero=models.IntegerField(primary_key=True)
    producto=models.TextField(blank=True, null=True)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField()
    senia=models.FloatField(null=True,blank=True)
    saldo=models.FloatField(null=True,blank=True)
    estado=models.TextField(choices=estado_pedido, default='Sin seña', max_length=100)
    cliente=models.ForeignKey(on_delete=models.CASCADE, to='core.Cliente', default=None,blank=True)
    presupuesto = models.IntegerField(null=True,blank=True)
    encargado = models.ForeignKey(on_delete=models.CASCADE, to=User, default=None,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)  

    @property
    def nombre_encargado(self):
        if self.encargado != None:
            return self.encargado.first_name
        else:
            return 'Sin asignar'

    def __str__(self):
        return str(self.numero)
    class META():
        ordering = ["-created"]
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

metodo_contacto = [ (0,'Visita local'), (1,'Whatsapp'), (2,'Instagram'), (3,'Facebook') ]
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    negocio = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=13, blank=True)
    direccion = models.CharField(max_length=200, blank=True, null=True, default=None)
    email = models.EmailField(max_length=100, blank=True)
    metodo_contacto=models.IntegerField(null=False,blank=False,choices=metodo_contacto, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.nombre
    class META():
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    @property
    def direccion_google(self):
        if self.direccion != None:
            direccion_google = "+".join(self.direccion.split(" "))
            return direccion_google

 
