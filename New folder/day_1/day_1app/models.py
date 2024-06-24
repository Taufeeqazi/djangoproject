from django.db import models

class signup(models.Model):
    Username=models.CharField(max_length=20,default='')
    email=models.EmailField(max_length=40)
    password1 = models.CharField(max_length=50)
    password2=models.CharField(max_length=50)



class login(models.Model):
    email=models.EmailField(max_length=40)
    password = models.CharField(max_length=50)