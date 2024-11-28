from django.db import models

class Productos(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=5)
    id_categoria = models.CharField(max_length=5)
    id_proveedor = models.CharField(max_length=5)
    nombre= models.CharField(max_length=20)
    precio= models.FloatField()
    talla= models.CharField(max_length=20)
    color= models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre