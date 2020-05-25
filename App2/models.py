from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    age = models.IntegerField(default=1)
