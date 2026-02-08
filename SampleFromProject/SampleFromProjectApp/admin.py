from django.contrib import admin
from .models import Employee
# Register your models here.
class Emp_Admin(admin.ModelAdmin):
    list_display = ('Emp_Id', 'Emp_name', 'Emp_email', 'Emp_position', 'Emp_phone')
admin.site.register(Employee, Emp_Admin)
