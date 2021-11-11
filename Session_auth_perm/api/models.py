from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    roll = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)