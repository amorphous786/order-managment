from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_id', 'customer_name', 'freight', 'ship_name', 'ship_country']
        widgets = {
            'order_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Order ID'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Customer Name'}),
            'freight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Freight Amount', 'step': '0.01'}),
            'ship_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Ship Name'}),
            'ship_country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Ship Country'}),
        }

    def clean_order_id(self):
        order_id = self.cleaned_data.get('order_id')
        if not order_id:
            raise forms.ValidationError("Order ID is required.")
        return order_id

    def clean_customer_name(self):
        customer_name = self.cleaned_data.get('customer_name')
        if not customer_name:
            raise forms.ValidationError("Customer name is required.")
        return customer_name

    def clean_freight(self):
        freight = self.cleaned_data.get('freight')
        if freight is None or freight <= 0:
            raise forms.ValidationError("Freight must be a positive number.")
        return freight 