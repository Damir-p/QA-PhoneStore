from django.db import models
from markets.models import Product, Location

class Customer(models.Model):
    first_name = models.CharField(max_length=100)    
    last_name = models.CharField(max_length=100)    
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=100)    
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = ("Клиент(Customer)")
        verbose_name_plural = ("Клиенты(Customers)")

    def __str__(self):
        return self.first_name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    tel_number = models.IntegerField()
    position = models.CharField(max_length=100)    
   
  
    class Meta:
        verbose_name = ("Сотрудник / Сотрудница(Employee)")
        verbose_name_plural = ("Сотрудники / Сотрудницы(Employees)")

    def __str__(self):
        return self.first_name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = ("Заказы(Order)")
        verbose_name_plural = ("Заказы(Orders)")

    def __str__(self):
        return f'{self.product} - {self.customer}'

    