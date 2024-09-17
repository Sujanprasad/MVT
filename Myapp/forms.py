from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_number', 'address']

class MembersForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class ValueForm(forms.Form):
    input_value = forms.IntegerField(label='Enter a value', min_value=0)

class Register_form(forms.ModelForm):
    password_confirm=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    class Meta:
        model=Register
        fields=['username','email','password']
        widgets = { 
            'password':forms.PasswordInput()
        }

class Login_form(forms.Form):
    username_or_email=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class EditDeleteForm(forms.ModelForm):
    name=forms.CharField(label="Enter a Name",max_length=25)
    class Meta:
        model=name
        fields=['name']
    
class emailform(forms.Form):
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    recipient_list = forms.CharField(widget=forms.Textarea, label="Enter target email(s)")

class Register_email_form(forms.ModelForm):
    password_confirm=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    class Meta:
        model=Register_email
        fields=['username','email','password']
        widgets = { 
            'password':forms.PasswordInput()
        }

class product_Registration(forms.Form):
    username=forms.CharField(max_length=25)
    email=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    password_confirm=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    CHOICES = (('None','None'),('admin', 'admin'),('user', 'user'),)
    panel = forms.ChoiceField(choices=CHOICES)
    
class product_login(forms.Form):
    email=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    CHOICES = (('None','None'),('admin', 'admin'),('user', 'user'),)
    panel = forms.ChoiceField(choices=CHOICES)

class Products_form(forms.ModelForm):
        class Meta:
          model=Product
          fields=['name','quality','quantity']

class Product_login_without_panel(forms.Form):
      email=forms.CharField()
      password=forms.CharField(widget=forms.PasswordInput)

class Questions_form(forms.ModelForm):
    CHOICES=(('None','None'),('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    Answer=forms.ChoiceField(choices=CHOICES)
    class Meta:
        model=Quiz_questions
        fields=['Question','Answer','Option1','Option2','Option3','Option4']

class Login_admin(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)