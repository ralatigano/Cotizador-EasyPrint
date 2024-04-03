from django.contrib import admin
from .models import Pedido, Cliente, Presupuesto

# Register your models here.

class AdminPresupuesto(admin.ModelAdmin):
    list_display = ["numero", "total", "saldo", "cliente","created", "updated"]
    search_fields = ["cliente", "numero", "created","total", "senia", "saldo"]
    list_filter = ["created", "cliente","updated","total"]
    list_per_page = 25
    readonly_fields=["numero","created", "updated"]

admin.site.register(Presupuesto, AdminPresupuesto)
class AdminPedidos(admin.ModelAdmin):
    list_display = ["numero", "producto", "descripcion", "precio", "senia", "saldo", "estado", "cliente", "presupuesto", "created"]
    search_fields = ["cliente", "producto", "estado"]
    list_filter = ["created", "producto","cliente", "estado"]
    list_per_page = 25
    readonly_fields=["created", "updated"]

admin.site.register(Pedido, AdminPedidos)

class AdminCLientes(admin.ModelAdmin):
    list_display = ["nombre", "negocio", "telefono", "email", "metodo_contacto", "created"]
    search_fields = ["nombre"]
    list_filter = ["created", "metodo_contacto"]
    list_per_page = 25
    readonly_fields=["created", "updated"]

admin.site.register(Cliente, AdminCLientes)
