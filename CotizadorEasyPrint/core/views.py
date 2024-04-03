
from typing import Any
from django.shortcuts import render, redirect
from .functions import *
from Products.models import Producto, Categoria
from .models import Presupuesto, Cliente, Pedido
from datetime import date
from django.contrib import messages

editando_presup = False
confirma = False
np_global = 0

# Create your views here.
def Inicio(request):
    global editando_presup 
    editando_presup = False
    global np_global
    total = 0
    descuento = 0
    totalNeto = 0
    np_global = 0
    pres = Presupuesto.objects.all()
    np=0
    for p in pres:
        if p.numero > np:
            np = p.numero
    np = np + 1
    ListProds = Producto.objects.all()
    Prods = Producto.objects.filter(presupuesto=None).filter(resultado__gt=0)
    for p in Prods:
        total += p.resultado
        descuento += p.desc_plata
        totalNeto = total-descuento
    Cat = Categoria.objects.all()
    data = {
        'np':np,
        'Cat':Cat,
        'ListProds':ListProds,
        'Prods':Prods,
        'total':total,
        'desc_plata':descuento,
        'totalNeto':totalNeto
    }
    return render(request, 'core/Inicio.html', data)

def Presupuestos(request):
    Pres = Presupuesto.objects.order_by('-numero').all()
    return render(request, 'core/Presupuestos.html', {'Pres': Pres})

def Pedidos(request):
    return render(request, 'core/Pedidos.html')

def Clientes(request):
    clientes = Cliente.objects.all().order_by('-created')
    return render(request, 'core/Clientes.html', {'clientes': clientes})

def Editar_Cliente(request):
    if request.method == 'POST':
        try:
            cliente = Cliente.objects.get(id=request.POST['id'])
            if cliente.nombre != request.POST['nombre']:
                cliente.nombre = request.POST['nombre']
            if cliente.negocio != request.POST['negocio']:
                cliente.negocio = request.POST['negocio']
            if cliente.telefono != request.POST['telefono']:
                cliente.telefono = request.POST['telefono']
            if cliente.direccion != request.POST['direccion']:
                cliente.direccion = request.POST['direccion']
            
            cliente.updated = date.today()
            cliente.save()
            messages.success(request, 'Cliente actualizado exitosamente')
        except Exception as e:
            messages.error(request, 'Error al actualizar el cliente. Error: ' + str(e))

        return redirect('/Clientes')

#Recibe el diccionario desde ObetenerDatos y decide de que forma se va a calcular el precio, según la categoría del producto.
def AgregarProducto(request):
    global editando_presup
    global np_global
    dict = {}

    dict = ObtenerDatos(request)
    caso_part = Producto.objects.filter(resultado=0).get(nombre=dict['producto']).caso_part
    if caso_part:
        costo = dict
    else:
        if dict['categoria'] == 'Papel':
            costo = Cal_Precio_Papel(dict)
        if dict['categoria'] == 'Vinilo':
            costo = Cal_Precio_Vinilo(dict)
        if dict['categoria'] == 'Lona':
            costo = Cal_Precio_LonaImpresa(dict)
        if dict['categoria'] == 'Vinilo-Stickers':
            costo = Cal_Precio_Stickers(dict)
        if dict['categoria'] == 'Pulseras':
            costo = Cal_Precio_Pulseras(dict)

    if editando_presup:
        url = f'/VerPresupuesto/{np_global}'
        costo['url'] = url
        Producto.objects.create(
        presupuesto = Presupuesto.objects.get(numero=np_global),
        cliente=costo['cliente'],
        nombre=costo['producto'],
        categoria=Categoria.objects.get(nombre=costo['categoria']),
        info_adic=costo['info_adic'],
        cantidad=costo['cantidad'],
        precio=costo['precio'], 
        desc_porcentaje=costo['descuento'],
        desc_plata=costo['desc_plata'], 
        resultado=costo['resultado']),
        costo['codigo'] = Producto.objects.last().codigo
        return render(request, 'core/Nuevo_calculo.html', costo) 
    else:
        url = '/'
        costo['url'] = url
        Producto.objects.create(
            presupuesto = None,
            cliente=costo['cliente'],
            nombre=costo['producto'],
            categoria=Categoria.objects.get(nombre=costo['categoria']),
            info_adic=costo['info_adic'],
            cantidad=costo['cantidad'],
            precio=costo['precio'], 
            desc_porcentaje=costo['descuento'],
            desc_plata=costo['desc_plata'], 
            resultado=costo['resultado']
            )
        costo['codigo'] = Producto.objects.last().codigo
        return render(request, 'core/Nuevo_calculo.html', costo) 

#Esta vista y la de EditarProducto son las que ayudan a editar un producto que está incluido en el presupuesto que se está elaborando.
def EditCalc_Presupuesto(request, r):
    prod = Producto.objects.get(codigo=r)
    Prods = Producto.objects.all()
    data = {
        'Prods':Prods,
        'prod':prod
    }
    return render(request, 'core/Editar_Item.html', data) # (Editar_Item)

def EditarProducto(request):
    #obtengo el producto a editar desde el request y lo traigo de la BD.
    codigo= request.POST['codigo']
    prod=Producto.objects.get(codigo=codigo)
    #Recibo los datos que podrían haberse modificado.
    producto = request.POST['edit_producto']
    info_adic = request.POST['info_adic']
    cantidad = int(request.POST['cantidad'])
    descuento = int(request.POST['descuento'])
    #Modifico el objeto del modelo con los nuevos datos:
    if prod.nombre != producto:
        prod.nombre = producto
        n_prod = Producto.objects.filter(prod.resultado==0).get(nombre=producto)
        prod.precio = n_prod.precio
    prod.info_adic = info_adic
    prod.cantidad = cantidad
    prod.desc_porcentaje = descuento
    prod.resultado = (int(cantidad)*float(prod.precio))*(1 - descuento/100)
    prod.desc_plata = cantidad * prod.precio * descuento / 100
    prod.save()
    if editando_presup:
        return redirect(f'/VerPresupuesto/{np_global}')
    else:
        return redirect( '/')
#Borra un ítem particular del presupuesto que se esta armando.
def DeleteCalc_Presupuesto(request, r):
    prod = Producto.objects.get(codigo=r)
    prod.delete()
    if editando_presup:
        return redirect(f'/VerPresupuesto/{np_global}')
    else:
        return redirect( '/')
#Borra todos los ítems del presupuesto que se está armando./Borra los elementos de la BD que no tienen un presupuesto asociado.
def DestroyCalc_Presupuesto(request):
    Calcs=Producto.objects.filter(presupuesto=None).filter(resultado__gt=0)
    for c in Calcs:
        if c.presupuesto != 0:
            c.delete()
    if editando_presup:
        pass
    else:
        return redirect( '/')

def GuardarPresupuesto(request):
    global editando_presup
    global np_global
    t = 0
    d = 0
    n_presupuesto = 3000000000 + Presupuesto.objects.count()
    if editando_presup:
        #Busco el presupuesto que estoy editando con ayuda de la variable global
        pre_v = Presupuesto.objects.get(numero=np_global)
        #Creo un nuevo presupuesto con el mismo cliente que el del presupuesto que estaba editando
        pre_n = Presupuesto.objects.create(
            numero=n_presupuesto,
            cliente=pre_v.cliente,
        )
        Prods = Producto.objects.filter(presupuesto=np_global)
        for p in Prods:
            p.presupuesto = Presupuesto.objects.get(numero=n_presupuesto)
            t = t + p.resultado
            d = d + p.desc_plata
            c = p.cliente
            p.save()
        #Actualizo el presupuesto con el valor total
        pre_n.total = t
        pre_n.save()

        return redirect('/Presupuestos')
    else:
        c = ''
        #Creo el presupuesto solo con el número de modo de poder asignárselo a los productos que perteneceran al nuevo presupuesto
        Presupuesto.objects.create(
            numero=n_presupuesto,
            cliente=None,
        )
        Prods = Producto.objects.all()
        for p in Prods:
            if p.presupuesto == None and p.resultado != 0:
                p.presupuesto = Presupuesto.objects.get(numero=n_presupuesto)
                t = t + p.resultado
                d = d + p.desc_plata
                c = p.cliente
                p.save()
        #Traigo el cliente desde la base de datos si es que existe y si no lo creo solo con nombre
        try:
            cli = Cliente.objects.get(nombre=c)
            #Actualizo el presupuesto con el valor total y el nombre del cliente
            pre= Presupuesto.objects.get(numero=n_presupuesto)
            pre.cliente = Cliente.objects.get(nombre=cli)
            pre.total = t
            pre.desc_plata = d
            pre.save()
        #Si el cliente no existe en la base de datos lo crea y actualiza la info del presupuesto
        except:
            Cliente.objects.create(
                nombre=c
            )
            #Actualizo el presupuesto con el valor total y el nombre del cliente
            pre= Presupuesto.objects.get(numero=n_presupuesto)
            pre.cliente = Cliente.objects.get(nombre=c)
            pre.total = t
            pre.desc_plata = d
            pre.save()
        #Si se utiliza el botón de generar pedido desde la vista de Inicio la bandera confirma es True para renderizar el template 'Completar_Pedido'.
        if confirma:
            n_ped = Armar_Numero_Pedido()
            Prods = Producto.objects.filter(presupuesto=n_presupuesto)
            lista = []
            for p in Prods:
                lista.append(f'{p.cantidad} {p.nombre}')
            data = {
                'np':n_presupuesto,
                'n_ped':n_ped,
                'cliente':c,
                'prods':lista,
                'total':t
            }
            return render(request, 'core/Completar_Pedido.html', data)
        else:
        #si no se utiliza el botón de generar pedido se redirecciona a la vista de Inicio después de crear el presupuesto con el botón 'Guardar presupuesto'.
            return redirect('/')
#Permite ver los elementos de un presupuesto para editarlos o para agregar mas ítems. Al guardar se generará un nuevo presupuesto.
def Editar_Presupuesto(request,np):
    global editando_presup
    editando_presup = True
    global np_global
    np_global = np
    Prods = Producto.objects.all()
    pres = Presupuesto.objects.get(numero=np)
    cli = pres.cliente
    Cat = Categoria.objects.all()
    data = {
        'Cat':Cat,
        'Prods':Prods,
        'np':np,
        'cli':cli,
    }
    return render(request, 'core/Editar_Presupuesto.html', data)

#Renderiza un formulario para completar detalles de un nuevo pedido. Crea un presupuesto. Registra un cliente si es nuevo.
def Completar_Pedido(request):
    global editando_presup
    n_ped = Armar_Numero_Pedido()

    if editando_presup:
        Prods = Producto.objects.filter(presupuesto=np_global)
        lista = []
        for p in Prods:
            lista.append(f'{p.cantidad} {p.nombre}')
        cli = Presupuesto.objects.get(numero=np_global).cliente
        total = Presupuesto.objects.get(numero=np_global).total
        data = {
            'n_ped':n_ped,
            'np' : np_global,
            'prods':lista,
            'cli':cli,
            'total':total
        }
        return render(request, 'core/Completar_Pedido.html', data)
    else:
        global confirma
        confirma = True
        return redirect('/GuardarPresupuesto')
    
#Crea un nuevo pedido con la info que se carga en el formulario del template Completar_Pedido.
def Confirmar_Pedido(request):
    pre = request.POST['total']
    se = request.POST['senia']
    list_p = []
    Prods = Producto.objects.filter(presupuesto=request.POST['n_presupuesto'])
    for p in Prods:
        list_p.append(f'{p.cantidad} {p.nombre},')
    print('ESTADO: ' + request.POST['estado'])
    Pedido.objects.create(
        numero = request.POST['n_pedido'],
        producto = list_p,
        descripcion = request.POST['info_adic'],
        precio = float(pre.replace(',','.')),
        senia = float(se.replace(',','.')),
        saldo = float(pre.replace(',','.')) - float(se.replace(',','.')),
        estado = request.POST['estado'],
        presupuesto = request.POST['n_presupuesto'],
        cliente = Presupuesto.objects.get(numero=request.POST['n_presupuesto']).cliente,
    )
    return redirect('/Pedidos')

#Lista los pedidos para verlos en una tabla
def Lista_Pedidos(request):
    Pedidos = Pedido.objects.order_by('numero').all()
    return render(request, 'core/Pedidos.html', {'Pedidos':Pedidos})

def Descargar_Presupuesto(request, np):
    Prods = Producto.objects.filter(presupuesto=np)
    cli = Presupuesto.objects.get(numero=np).cliente
    fecha = date.today()
    total = Presupuesto.objects.get(numero=np).total
    descuento = Presupuesto.objects.get(numero=np).desc_plata
    imgEncabezado =  'core/img/encabezado.jpg'
    data = {
        'Prods':Prods,
        'dia':fecha.day,
        'mes':fecha.month,
        'anio':str(fecha.year)[2:4],
        'np':np,
        'cliente':cli,
        'total':total,
        'desc_plata':descuento,
        'imgEncabezado':imgEncabezado
    }
    return render(request, 'core/Descargar_Presupuesto.html', data)

def Cambiar_estado(request):
    if request.POST['estado'] != 'Elegir un estado':
        n_pedido = request.POST['cambiarPedido_estado']
        pedido = Pedido.objects.get(numero=n_pedido)
        pedido.estado = request.POST['estado']
        pedido.save()
    return redirect('/Pedidos')

def Cambiar_enc(request):
    if request.POST['encargado'] != 'Elegir un encargado':
        n_pedido = request.POST['cambiarPedido_enc']
        pedido = Pedido.objects.get(numero=n_pedido)
        pedido.encargado = User.objects.get(username=request.POST['encargado'])
        pedido.save()
    return redirect('/Pedidos')

def Agregar_descripcion(request):
    if request.POST['descripcion'] != '':
        n_pedido = request.POST['cambiarPedido_desc']
        pedido = Pedido.objects.get(numero=n_pedido)
        pedido.descripcion = pedido.descripcion + '//' + request.POST['descripcion']
        pedido.save()
    return redirect('/Pedidos')

def Agregar_senia(request):
    if request.POST['senia'] != '':
        n_pedido = request.POST['cambiarPedido_senia']
        pedido = Pedido.objects.get(numero=n_pedido)
        nuev_senia = float(request.POST['senia'].replace(',','.'))
        pedido.senia = pedido.senia + nuev_senia
        pedido.saldo = pedido.precio - pedido.senia
        pedido.save()
    return redirect('/Pedidos')
    