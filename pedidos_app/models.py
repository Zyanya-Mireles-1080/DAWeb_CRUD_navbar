from django.db import models

class Pedidos(models.Model):
    id_pedido = models.CharField(primary_key=True, max_length=5)
    id_cliente = models.CharField(max_length=5)
    id_empleado = models.CharField(max_length=5)
    fecha = models.DateField(verbose_name="Fecha del pedido", null=False, blank=False)
    total = models.CharField(max_length=1000000)
    metodo_pago= models.CharField(max_length=20)
    horario = models.TimeField(verbose_name="Horario", auto_now=False, auto_now_add=False)
    cantidad = models.CharField(max_length=1000)

    def __str__(self):
        return self.id_pedido

