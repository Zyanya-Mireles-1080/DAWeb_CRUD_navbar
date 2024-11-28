from django.shortcuts import render, redirect
from .models import Categoria

# Create your views here.

def inicio_vistaCategorias(request):
    lascategorias = Categoria.objects.all()

    return render(request,"gestionarCategorias.html",{"lascategorias":lascategorias})

def registrarCategorias(request):
    id_categoria = request.POST["idcategoria"]
    id_proveedor = request.POST["idproveedor"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    cantidad = request.POST["intcantidad"]
    promocion = request.POST["txtpromocion"]
    audiencia = request.POST["txtaudiencia"]

    guardarcategorias=Categoria.objects.create(id_categoria=id_categoria, id_proveedor=id_proveedor, nombre=nombre, descripcion=descripcion, cantidad=cantidad, 
    promocion=promocion, audiencia=audiencia)
    return redirect("categorias")

def seleccionarCategorias(request,id_categoria):
    categorias = Categoria.objects.get(id_categoria=id_categoria)
    return render(request,"editarCategorias.html",{"lascategorias":categorias})

def editarCategorias(request):
    id_categoria = request.POST["idcategoria"]
    id_proveedor = request.POST["idproveedor"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    cantidad = request.POST["intcantidad"]
    promocion = request.POST["txtpromocion"]
    audiencia = request.POST["txtaudiencia"]

    categorias = Categoria.objects.get(id_categoria=id_categoria)
    categorias.id_proveedor = id_proveedor
    categorias.nombre = nombre
    categorias.descripcion = descripcion
    categorias.cantidad = cantidad
    categorias.promocion = promocion
    categorias.audiencia = audiencia

    categorias.save()
    return redirect("categorias")

def borrarCategorias(request,id_categoria):
    categorias = Categoria.objects.get(id_categoria=id_categoria)
    categorias.delete()

    return redirect("categorias")
