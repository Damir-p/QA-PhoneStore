from django.forms import ModelForm, forms
from .models import Order, Customer, Employee


class CustomerForm(ModelForm):
    class meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'gender': forms.Select(choices=Employee.GENDER_CHOICES),
        }


class EmployeeForm(ModelForm):
    class meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'gender': forms.Select(choices=Employee.GENDER_CHOICES),
        }
        
class OrderForm(ModelForm):
    class meta:
        model = Order
        fields = '__all__'