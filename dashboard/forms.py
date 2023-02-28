from django.forms import ModelForm, forms, GENDER_CHOICES
from .models import Order, Customer, Employee


class CustomerForm(ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    class meta:
        model = Customer
        fields = fields = ['name', 'age', 'location', 'gender']
     
class EmployeeForm(ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)    
    class meta:
        model = Employee
        fields = fields = ['name', 'age', 'location', 'gender']
 
class OrderForm(ModelForm):
    class meta:
        model = Order
        fields = '__all__'