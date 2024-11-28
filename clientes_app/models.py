from django.db import models

class Clientes(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=10)
    fecha_registro = models.DateField(verbose_name="Fecha de registro", null=False, blank=False)
    
    def __str__(self):
        return self.nombre
