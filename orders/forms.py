from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Postal_code'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City'}))
    class Meta:
        model = Order
        fields = ['first_name','last_name', 'email', 'address',
                  'postal_code', 'city']