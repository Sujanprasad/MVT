from django.db import models

class Registrations(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=500)
    def __str__(self):
        return f'{self.username}'   