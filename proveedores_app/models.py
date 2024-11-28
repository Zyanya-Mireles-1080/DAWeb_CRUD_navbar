from django.db import models

class Proveedores(models.Model):
    id_proveedor = models.CharField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=30)
    tipo_producto = models.CharField(max_length=20)
    ref_pago = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre