from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=50)
    add=models.CharField(max_length=100)
    subjects=models.CharField(max_length=20)
    marks=models.IntegerField()