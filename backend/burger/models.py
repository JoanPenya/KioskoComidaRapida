from django.db import models

class Customer(models.Model):
   id = models.BigAutoField(primary_key=True)
   servicio = models.CharField(max_length=100)
   pago = models.CharField(max_length=100)

class Product(models.Model):
   id = models.BigAutoField(primary_key=True)
   name = models.CharField(max_length=100)
   imagen = models.TextField()
   tipo = models.CharField(max_length=100)
   precio = models.IntegerField()

class CxP(models.Model):
   IdCustomer = models.ForeignKey(Customer, on_delete=models.CASCADE)
   IdProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
   unidad = models.IntegerField()