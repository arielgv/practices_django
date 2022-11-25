from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(verbose_name="Full Name", max_length=100)
    email = models.EmailField(blank=True, null=True)
    fone = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre


class Items(models.Model):

    nombre = models.CharField(max_length=200)
    seccion = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f'The name is {self.nombre}, seccion is {self.seccion} and the price is {self.price}.'

class Pedido(models.Model):

    num_pedido = models.IntegerField()
    fecha =models.DateField()
    entregado = models.BooleanField()
 
