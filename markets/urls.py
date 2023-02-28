from django.urls import path
from .models import Location, Product

urlpatterns = [
    path('location/', Location),
    path('product/', Product),
]