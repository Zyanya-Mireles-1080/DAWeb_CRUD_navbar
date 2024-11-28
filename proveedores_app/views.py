from django.shortcuts import render, redirect
from .models import Proveedores

# Create your views here.

def inicio_vistaProveedores(request):
    losproveedores = Proveedores.objects.all()

    return render(request,"gestionarProveedores.html",{"losproveedores":losproveedores})

def registrarProveedores(request):
    id_proveedor = request.POST["idproveedor"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["intelefono"]
    correo = request.POST["txtcorreo"]
    direccion = request.POST["txtdireccion"]
    tipo_producto = request.POST["txtproducto"]
    ref_pago = request.POST["txtref"]

    guardarproveedores=Proveedores.objects.create(id_proveedor=id_proveedor, nombre=nombre, telefono=telefono, correo=correo, direccion=direccion,
    tipo_producto=tipo_producto, ref_pago=ref_pago)
    return redirect("proveedores")

def seleccionarProveedores(request,id_proveedor):
    proveedores = Proveedores.objects.get(id_proveedor=id_proveedor)
    return render(request,"editarProveedor.html",{"losproveedores":proveedores})

def editarProveedores(request):
    id_proveedor = request.POST["idproveedor"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["intelefono"]
    correo = request.POST["txtcorreo"]
    direccion = request.POST["txtdireccion"]
    tipo_producto = request.POST["txtproducto"]
    ref_pago = request.POST["txtref"]
    proveedores = Proveedores.objects.get(id_proveedor=id_proveedor)
    proveedores.nombre = nombre
    proveedores.telefono = telefono
    proveedores.correo = correo
    proveedores.direccion = direccion
    proveedores.tipo_producto = tipo_producto
    proveedores.ref_pago = ref_pago
    proveedores.save()
    return redirect("proveedores")

def borrarProveedores(request,id_proveedor):
    proveedores = Proveedores.objects.get(id_proveedor=id_proveedor)
    proveedores.delete()

    return redirect("proveedores")