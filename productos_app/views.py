from django.shortcuts import render, redirect
from .models import Productos

# Create your views here.

def inicio_vistaProductos(request):
    losproductos = Productos.objects.all()

    return render(request,"gestionarProductos.html",{"losproductos":losproductos})

def registrarProductos(request):
    id_producto = request.POST["idproducto"]
    id_categoria = request.POST["idcategoria"]
    id_proveedor = request.POST["idproveedor"]
    nombre= request.POST["txtnombre"]
    precio= request.POST["floatprecio"]
    talla= request.POST["txtalla"]
    color= request.POST["txtcolor"]

    guardarproductos=Productos.objects.create(id_producto=id_producto, id_categoria=id_categoria, id_proveedor=id_proveedor, nombre=nombre,
    precio=precio, talla=talla, color=color)
    return redirect("productos")

def seleccionarProductos(request,id_producto):
    productos = Productos.objects.get(id_producto=id_producto)
    return render(request,"editarProductos.html",{"losproductos":productos})

def editarProductos(request):
    id_producto = request.POST["idproducto"]
    id_categoria = request.POST["idcategoria"]
    id_proveedor = request.POST["idproveedor"]
    nombre= request.POST["txtnombre"]
    precio= request.POST["floatprecio"]
    talla= request.POST["txtalla"]
    color= request.POST["txtcolor"]
    productos = Productos.objects.get(id_producto=id_producto)
    productos.id_categoria = id_categoria
    productos.id_proveedor= id_proveedor
    productos.nombre = nombre
    productos.precio = precio
    productos.talla = talla
    productos.color = color
    productos.save()
    return redirect("productos")

def borrarProductos(request,id_producto):
    productos = Productos.objects.get(id_producto=id_producto)
    productos.delete()

    return redirect("productos")