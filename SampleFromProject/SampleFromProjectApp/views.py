from django.shortcuts import render

from SampleFromProjectApp.forms import EmployeeForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_employee(request):
    form=EmployeeForm()
    if request.method == 'POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'add_employee.html', context={'form':form})