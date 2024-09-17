from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



class RegisterAdminForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1=forms.CharField(label="Password",widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    is_staff= forms.BooleanField(label="staff Status",required=False)
    is_superuser= forms.BooleanField(label="Superuser Status",required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','is_staff','is_superuser']

class Login_admin(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class Registration(forms.Form):
    username=forms.CharField()
    email = forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)