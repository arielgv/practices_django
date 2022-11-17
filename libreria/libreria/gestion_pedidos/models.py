from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    fone = models.CharField(max_length=25)



class Items(models.Model):

    nombre = models.CharField(max_length=200)
    stock = models.IntegerField()
    price = models.IntegerField()


class Pedido(models.Model):

    num_pedido = models.IntegerField()
    entregado = models.BooleanField()

