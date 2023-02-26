from django.urls import path
from .models import Order, Customer, Employee
from .views import (
    
    customer_list, 
    customer_create, 
    customer_update, 
    customer_delete,
    
    employee_list,
    employee_create,
    employee_update,
    employee_delete,
    
    order_list,
    order_create,
    order_update,
    order_delete,
)

urlpatterns = [
    path('orders/',Order),
    path('employees/', Employee),
    path('customers/', Customer),
    
    path('customer_create/', customer_create),
    path('customer_list/', customer_list),
    path('customer_update/', customer_update),
    path('customer_delete/', customer_delete),


    path('employee_create/', employee_create),
    path('employee_list/', employee_list),
    path('employee_update/', employee_update),
    path('employee_delete/', employee_delete),


    path('order_create/', order_create),
    path('order_list/', order_list),
    path('order_update/', order_update),
    path('order_delete/', order_delete),

]


