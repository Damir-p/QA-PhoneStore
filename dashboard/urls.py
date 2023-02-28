# urls.py
from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView
from .views import EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView
from .views import OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView


urlpatterns = [
    path('customer/', CustomerListView.as_view(), name='customer_list'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
    
    path('employee/', EmployeeListView.as_view(), name='employee_list'),
    path('employee/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
   
    path('order/', OrderListView.as_view(), name='order_list'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
]

