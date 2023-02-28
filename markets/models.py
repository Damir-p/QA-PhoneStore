from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    areas = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    
    
    class Meta:
        verbose_name = ("Location")
        verbose_name_plural = ("Locations")

    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desctiption = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Product")

    def __str__(self):
        return self.name
    
    