from django import forms
from django.utils.translation import gettext_lazy as _


class CouponApplyForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Coupon', 'style': 'width: 170px;', 'border-radius': '25px;', 'border-color': 'red'}))