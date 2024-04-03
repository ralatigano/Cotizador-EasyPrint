from django.urls import path
from .views import Productos, Cargar_Productos, Editar_Producto, Borrar_Producto

urlpatterns = [
    path('', Productos, name='Productos'),
    path('CargarProductos', Cargar_Productos, name='Cargar_Productos'),
    path('EditarProducto', Editar_Producto, name='EditarProducto'),
    path('BorrarProducto/<int:producto_id>', Borrar_Producto, name='BorrarProducto'),
]