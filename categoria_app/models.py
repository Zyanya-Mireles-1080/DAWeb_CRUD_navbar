from django.db import models

class Categoria(models.Model):
    id_categoria = models.CharField(primary_key=True, max_length=5)
    id_proveedor = models.CharField(max_length=5)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    promocion = models.CharField(max_length=30)
    audiencia = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre
