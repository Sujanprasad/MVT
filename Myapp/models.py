
# Create your models here.
from django.db import models

class Member(models.Model):
   firstname = models.CharField(max_length=255)
   lastname = models.CharField(max_length=255)
   phone=models.IntegerField(null=True)

   def __str__(self):
      return f"{self.firstname}"
   
class Emp(models.Model):
   firstname=models.CharField(max_length=25)
   lastname=models.CharField(max_length=25)
   phone=models.IntegerField(null=True)
   salary=models.IntegerField(null=True)
   position=models.CharField(max_length=25,null=True)

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class ValueStore(models.Model):
    value = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.value}'
    
class Register(models.Model):
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=8)
    def __str__(self):
        return f'{self.username}'
    
class USER(models.Model):
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=8)

class name(models.Model):
    name=models.CharField(max_length=25,unique=True) 
    
class Register_email(models.Model):
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=8)
    def __str__(self):
        return f'{self.username}'
    
class Product_admin(models.Model):
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField()
    password=models.CharField(max_length=8)
    def __str__(self):
        return f'{self.username}'    
    
class Product_user(models.Model):
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField()
    password=models.CharField(max_length=8)
    def __str__(self):
        return f'{self.username}'    

class Product(models.Model):
    name=models.CharField(max_length=25)
    quality=models.IntegerField()
    quantity=models.IntegerField()
    def __str__(self):
        return f'{self.name}'   


class Quiz_questions(models.Model):
    Question=models.CharField(max_length=250)
    Answer=models.CharField(max_length=50)
    Option1=models.CharField(max_length=50)
    Option2=models.CharField(max_length=50)
    Option3=models.CharField(max_length=50)
    Option4=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.Question}'   