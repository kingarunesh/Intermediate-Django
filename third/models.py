from django.db import models


class FirstModel(models.Model):
    # name = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)