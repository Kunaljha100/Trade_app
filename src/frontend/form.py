from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

from trading_component.models import order
User = get_user_model()


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = order
        fields = (
            'entry_price',
            "quantity", 
            "trade_type",
            "user",
            

            
        )



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

    