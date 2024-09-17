from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password,check_password

def register_admin(request):
    if request.method == 'POST':
        form=RegisterAdminForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=RegisterAdminForm()    
    return render(request, 'Register_admin.html', {'form': form})


def login_admin(request):
    if request.method == 'POST':
        form = Login_admin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password) 
            if user is not None:
                print(user)
                login(request, user)
                return redirect('/admin')
            else:
                form.add_error(None, "Invalid email or password")
    else:
        form = Login_admin()
    return render(request, 'Login_admin.html', {'form': form})

def Register(request):
    if request.method == 'POST':
        form=Registration(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email=request.POST['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password==confirm_password:
                encryptedpassword=make_password(password)
                print(encryptedpassword)
                if Registrations.objects.filter(username=username).exists()|User.objects.filter(username=username).exists():
                    form.add_error(None,"user already exists")
                else:
                    Registrations.objects.create(username=username,email=email,password=encryptedpassword)
                    User.objects.create_superuser(username=username,email=email,password=password)
            else:
                form.add_error('password2',"passwords not matching")
    else:
        form=Registration()    
  
    return render(request, 'Registrations.html', {'form': form})

def sample(request):
    return render(request,'abc.html',{'fruits':"apple"})