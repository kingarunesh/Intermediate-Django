from django.db import models


class FirstModel(models.Model):
    # name = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)



class SecondModel(models.Model):
    # name = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)



class User(models.Model):
    t_name = models.CharField(max_length=100)
    s_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)