from django.shortcuts import render, redirect
from .models import Pedidos

# Create your views here.

def inicio_vistaPedidos(request):
    lospedidos = Pedidos.objects.all()
    return render(request,"gestionarPedidos.html",{"lospedidos":lospedidos})

def registrarPedidos(request):
    id_pedido=request.POST["idpedido"]
    id_cliente=request.POST["idcliente"]
    id_empleado = request.POST["idempleado"]
    fecha=request.POST["datefecha"]
    total = request.POST["numtotal"]
    metodo_pago = request.POST["txtmetodopago"]
    horario = request.POST["datehora"]
    cantidad = request.POST["numcantidad"]

    guardarpedidos=Pedidos.objects.create(id_pedido=id_pedido, id_cliente=id_cliente, id_empleado=id_empleado, fecha=fecha,
    total = total, metodo_pago = metodo_pago, horario = horario, cantidad = cantidad)
    return redirect("pedidos")

def seleccionarPedidos(request,id_pedido):
    pedidos = Pedidos.objects.get(id_pedido=id_pedido)
    return render(request,"editarPedidos.html",{"lospedidos":pedidos})

def editarPedidos(request):
    id_pedido=request.POST["idpedido"]
    id_cliente=request.POST["idcliente"]
    id_empleado = request.POST["idempleado"]
    fecha=request.POST["datefecha"]
    total = request.POST["numtotal"]
    metodo_pago = request.POST["txtmetodopago"]
    horario = request.POST["datehora"]
    cantidad = request.POST["numcantidad"]
    pedidos = Pedidos.objects.get(id_pedido=id_pedido)
    pedidos.id_cliente = id_cliente
    pedidos.id_empleado = id_empleado
    pedidos.fecha = fecha
    pedidos.total = total
    pedidos.metodo_pago = metodo_pago
    pedidos.horario = horario
    pedidos.cantidad = cantidad
    pedidos.save()
    return redirect("pedidos")

def borrarPedidos(request,id_pedido):
    pedidos = Pedidos.objects.get(id_pedido=id_pedido)
    pedidos.delete()
    return redirect("pedidos")