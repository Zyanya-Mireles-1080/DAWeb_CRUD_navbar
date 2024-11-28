from django.shortcuts import render, redirect
from .models import Empleados

# Create your views here.

def inicio_vistaEmpleados(request):
    losempleados = Empleados.objects.all()

    return render(request,"gestionarEmpleados.html",{"losempleados":losempleados})

def registrarEmpleados(request):
    id_empleado = request.POST["idempleado"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["intelefono"]
    correo = request.POST["txtcorreo"]
    direccion = request.POST["txtdireccion"]
    turno = request.POST["txtturno"]
    sueldo = request.POST["intsueldo"]

    guardarempleados=Empleados.objects.create(id_empleado=id_empleado, nombre=nombre, telefono=telefono, correo=correo, direccion=direccion,
    turno=turno, sueldo=sueldo)
    return redirect("empleados")

def seleccionarEmpleados(request,id_empleado):
    empleados = Empleados.objects.get(id_empleado=id_empleado)
    return render(request,"editarEmpleados.html",{"losempleados":empleados})

def editarEmpleados(request):
    id_empleado = request.POST["idempleado"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["intelefono"]
    correo = request.POST["txtcorreo"]
    direccion = request.POST["txtdireccion"]
    turno = request.POST["txtturno"]
    sueldo = request.POST["intsueldo"]

    empleados = Empleados.objects.get(id_empleado=id_empleado)
    empleados.nombre = nombre
    empleados.telefono = telefono
    empleados.correo = correo
    empleados.direccion = direccion
    empleados.turno = turno
    empleados.sueldo = sueldo
    empleados.save()
    return redirect("empleados")

def borrarEmpleados(request,id_empleado):
    empleados = Empleados.objects.get(id_empleado=id_empleado)
    empleados.delete()

    return redirect("empleados")
