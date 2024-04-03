from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Producto, Categoria
import csv
from django.core.files.storage import FileSystemStorage
from .functions import *
from django.contrib import messages


# Create your views here.
# def List_Products(_request):


def Productos(request):
    prods=Producto.objects.filter(resultado=0).all()
    return render(request, 'core/Productos.html', {'prods':prods})


def Cargar_Productos(request):
    total = 0
    contador = 0
    try:
        if request.method == 'POST' and request.FILES.get('csv_file'):
            csv_file = request.FILES['csv_file']
            fs = FileSystemStorage()
            filename = fs.save(csv_file.name, csv_file)

            with fs.open(filename, 'r') as file:
                csv_data = csv.reader(file)
                next(csv_data)
                for row in csv_data:
                    total += 1
                    codigo, nombre, ancho, alto, precio, categoria = row
                    comparacion = comparar(codigo)
                    n = nombre.strip()
                    a = ancho.strip()
                    p = precio.strip()
                    c = categoria.strip()
                    if comparacion != True:
                        contador += 1
                        Producto.objects.create(
                            codigo=codigo,
                            nombre=n,
                            ancho=a,
                            alto=alto,
                            precio=p,
                            categoria=Categoria.objects.get(nombre=c)
                        )

            # Eliminar el archivo cargado después de procesarlo
            fs.delete(filename)
            messages.success(request, f'Se han cargado {contador} de {total} productos correctamente.')
    except Exception as e:
        messages.error(request, f'No se han podido cargar los productos. Error({e})')
    return redirect('/Productos', messages)

def Editar_Producto(request):
    if request.method == 'POST':
        if request.POST['codigo'] != '':
            try:
                info = "|".join(request.POST.values())
                info = info.split('|')
                p = Producto.objects.get(pk=request.POST['codigo'])
                if p.nombre != info[2]:
                    p.nombre = info[2]
                if p.ancho != info[5]:
                    p.ancho = info[5].replace(',','.')
                if p.alto != info[6]:
                    p.alto = info[6].replace(',','.')
                if p.precio != info[3]:
                    p.precio = info[3].replace(',','.')
                if p.categoria.nombre != info[4]:
                    p.categoria = Categoria.objects.get(nombre = info[4])
                if 'caso_part' in request.POST:
                    p.caso_part = True
                else:
                    p.caso_part = False
                p.save()
                messages.success(request, 'Los datos del producto se han actualizado correctamente.')
            except Exception as e:
                messages.error(request, f'No se ha podido actualizar los datos del producto. Error({e})')
        else:
            try:
                p = Producto.objects.create(
                    presupuesto = None,
                    nombre = request.POST['nombre_add'],
                    ancho = request.POST['ancho_add'],
                    alto = request.POST['alto_add'],
                    precio = request.POST['precio_add'],
                    categoria = Categoria.objects.get(nombre = request.POST['categ_add']),
                )
                messages.success(request, 'El nuevo producto se ha agregado correctamente.')
            except Exception as e:
                messages.error(request, f'No se ha podido agregar el nuevo producto. Error({e})')
    return redirect('/Productos', messages)
def Borrar_Producto(request, producto_id):
    try:
        prod = Producto.objects.filter(pk=producto_id)
        prod.delete()
        messages.success(request, 'El producto se ha borrado correctamente.')
    except Exception as e:
        messages.error(request, f'No se ha podido borrar el producto. Error({e})')
    return redirect('/Productos', messages)
