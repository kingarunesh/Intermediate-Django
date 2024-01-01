from django.db import models


class Student(models.Model):
    """
        student table
    """
    student_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    marks = models.CharField(max_length=100)
    section = models.CharField(max_length=10, default="A")
