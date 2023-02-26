from django import forms
from .models import Order, Customer, Employee
from  markets.models import Product

class CustomerForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    date_ordered = forms.DateField(widget=forms.DateInput())

    class Meta:
        model = Customer
        fields = ['product', 'employee', 'customer', 'date_ordered']

    def save(self, commit=True):
        customer = super().save(commit=False)
        if commit:
            customer.save()
        return customer
    
    
class EmployeeForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    date_ordered = forms.DateField(widget=forms.DateInput())

    class Meta:
        model = Employee
        fields = ['product', 'employee', 'customer', 'date_ordered']

    def save(self, commit=True):
        employee = super().save(commit=False)
        if commit:
            employee.save()
        return employee
    
    
class OrderForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    date_ordered = forms.DateField(widget=forms.DateInput())

    class Meta:
        model = Order
        fields = ['product', 'employee', 'customer', 'date_ordered']

    def save(self, commit=True):
        order = super().save(commit=False)
        if commit:
            order.save()
        return order
    
    
    

    
    
    
