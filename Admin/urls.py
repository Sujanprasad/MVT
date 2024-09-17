from django.urls import path
from .views import *

urlpatterns = [

path('register_admin/',register_admin,name="Register_admin"),
path('login_admin/',login_admin,name="Login admin"),
path('Registrations/',Register),
path('css/',sample)
]