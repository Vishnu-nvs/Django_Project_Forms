from django.db import models

# Create your models here.
class Employee(models.Model):
    Emp_Id =models.PositiveIntegerField()
    Emp_name = models.CharField(max_length=30)
    Emp_email = models.EmailField(unique=True)
    Emp_position = models.CharField(max_length=50)
    Emp_phone = models.CharField(max_length=15)     
