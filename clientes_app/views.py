from django.shortcuts import render, redirect
from .models import Clientes

# Create your views here.

def inicio_vistaClientes(request):
    losclientes = Clientes.objects.all()

    return render(request,"gestionarClientes.html",{"losclientes":losclientes})

def registrarClientes(request):
    id_cliente = request.POST["idcliente"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["intelefono"]
    correo = request.POST["txtcorreo"]
    direccion = request.POST["txtdireccion"]
    contraseña = request.POST["txtcontraseña"]
    fecha_registro = request.POST["datefecha"]

    guardarclientes=Clientes.objects.create(id_cliente=id_cliente, nombre=nombre, telefono=telefono, correo=correo, direccion=direccion,
    contraseña=contraseña, fecha_registro=fecha_registro)
    return redirect("clientes")

def seleccionarClientes(request,id_cliente):
    clientes = Clientes.objects.get(id_cliente=id_cliente)
    return render(request,"editarClientes.html",{"losclientes":clientes})

def editarClientes(request):
    id_cliente = request.POST["idcliente"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["intelefono"]
    correo = request.POST["txtcorreo"]
    direccion = request.POST["txtdireccion"]
    contraseña = request.POST["txtcontraseña"]
    fecha_registro = request.POST["datefecha"]
    clientes = Clientes.objects.get(id_cliente=id_cliente)
    clientes.nombre = nombre
    clientes.telefono = telefono
    clientes.correo = correo
    clientes.direccion = direccion
    clientes.contraseña = contraseña
    clientes.fecha_registro = fecha_registro
    clientes.save()
    return redirect("clientes")

def borrarClientes(request,id_cliente):
    clientes = Clientes.objects.get(id_cliente=id_cliente)
    clientes.delete()

    return redirect("clientes")