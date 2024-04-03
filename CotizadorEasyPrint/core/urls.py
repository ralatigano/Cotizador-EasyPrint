
from django.urls import path
from .views import (
                    Inicio, Presupuestos, AgregarProducto, DeleteCalc_Presupuesto, EditCalc_Presupuesto, 
                    EditarProducto, DestroyCalc_Presupuesto, GuardarPresupuesto, Editar_Presupuesto, Confirmar_Pedido, 
                    Completar_Pedido, Lista_Pedidos, Descargar_Presupuesto, Cambiar_estado, Cambiar_enc, Agregar_descripcion,
                    Agregar_senia, Clientes, Editar_Cliente
)


urlpatterns = [
    path('', Inicio, name='Inicio'),
    path('Clientes', Clientes, name='Clientes'),
    path('Presupuestos', Presupuestos, name='Presupuestos'),
    path('AgregarProducto', AgregarProducto, name='AgregarProducto'),
    path('DeleteCalc_Presupuesto/<str:r>/', DeleteCalc_Presupuesto, name='DeleteCalc_Presupuesto'),
    path('EditCalc_Presupuesto/<int:r>/', EditCalc_Presupuesto, name='EditCalc_Presupuesto'),
    path('EditarProducto', EditarProducto, name='EditarProducto'),
    path('BorrarTodo', DestroyCalc_Presupuesto, name='BorrarTodo'),
    path('GuardarPresupuesto', GuardarPresupuesto, name='GuardarPresupuesto'),
    path('VerPresupuesto/<int:np>/', Editar_Presupuesto, name='VerPresupuesto'),
    path('ConfirmarPedido', Confirmar_Pedido, name='Confirmar_Pedido'),
    path('CompletarPedido', Completar_Pedido, name='CompletarPedido'),
    path('Pedidos', Lista_Pedidos, name='Pedidos'),
    path('DescargarPresupuesto/<int:np>', Descargar_Presupuesto, name='DescargarPresupuesto'),
    path('CambiarEstado', Cambiar_estado, name='CambiarEstado'),
    path('CambiarEncargado', Cambiar_enc, name='CambiarEncargado'),
    path('AgregarDescripcion', Agregar_descripcion, name='Agregar_descripcion'),
    path('AgregarSenia', Agregar_senia, name='Agregar_senia'),
    path('EditarCliente', Editar_Cliente, name='Editar_Cliente'),
]