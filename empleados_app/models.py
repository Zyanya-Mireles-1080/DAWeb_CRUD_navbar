from django.db import models

class Empleados(models.Model):
    id_empleado = models.CharField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=30)
    turno = models.CharField(max_length=30)
    sueldo = models.IntegerField()
    
    def __str__(self):
        return self.nombre