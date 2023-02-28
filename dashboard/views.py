from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Customer, Employee, Order


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customer'


class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['name', 'age', 'gender', 'location']
    success_url = reverse_lazy('customer_list')



class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_delete.html'
    success_url = reverse_lazy('customer_list')

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['name', 'age', 'gender', 'location']
    success_url = reverse_lazy('customer_list')



class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'
    context_object_name = 'employee'

class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee_form.html'
    fields = ['name', 'age', 'gender', 'location']
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_delete.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee_form.html'
    fields = ['name', 'age', 'gender', 'location']
    success_url = reverse_lazy('employee_list')



class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_form.html'
    fields = ['customer', 'employee', 'product']
    success_url = reverse_lazy('order_list')
    

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_delete.html'
    success_url = reverse_lazy('order_list')


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_form.html'
    fields = ['customer', 'employee', 'product']
    success_url = reverse_lazy('order_list')


