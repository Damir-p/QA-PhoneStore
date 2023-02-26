from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Employee, Order
from .forms import CustomerForm, EmployeeForm

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'dashboard/customer_list.html', {'customers': customers})

def customer_create(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, 'dashboard/customer_form.html', {'form': form})

def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, 'dashboard/customer_form.html', {'form': form})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'dashboard/customer_confirm_delete.html', {'customer': customer})




def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'dashboard/employee_list.html', {'employees': employees})

def employee_create(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'dashboard/employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'dashboard/employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'dashboard/employee_confirm_delete.html', {'employee': employee})




# def order_list(request):
#     orders = Order.objects.all()
#     return render(request, 'dashboard/order_list.html', {'orders': orders})

# def order_create(request):
#     form = OrderForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('order_list')
#     return render(request, 'dashboard/order_form.html', {'form': form})

# def order_update(request, pk):
#     order = get_object_or_404(Order, pk=pk)
#     form = OrderForm(request.POST or None, instance=order)
#     if form.is_valid():
#         form.save()
#         return redirect('order_list')
#     return render(request, 'dashboard/order_form.html', {'form': form})

# def order_delete(request, pk):
#     order = get_object_or_404(Order, pk=pk)
#     if request.method == 'POST':
#         order.delete()
#         return redirect('order_list')
#     return render(request, 'dashboard/order_confirm_delete.html', {'order': order})


