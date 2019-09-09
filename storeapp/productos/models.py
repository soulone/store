from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_categoria = models.TextField()
    nombre_producto = models.TextField(max_length=50)
    precio_producto = models.IntegerField()
    stock = models.IntegerField()


class Admin(models.Model):
    id_admin =  models.AutoField(primary_key=True)
    usuario =  models.TextField(max_length=25)
    pass_usuario = models.TextField()