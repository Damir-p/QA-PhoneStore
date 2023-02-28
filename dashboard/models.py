from django.db import models
from markets.models import Product, Location

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]

class Customer(models.Model):
    name = models.CharField(max_length=100)        
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)    

    def __str__(self):
        return self.first_name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.first_name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    
  
    def __str__(self):
        return f'{self.product} - {self.customer}'

    