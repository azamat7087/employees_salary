from django.shortcuts import render
from .models import *
import math
from django.views import View
# Create your views here.


class ChangeSalary(View):
    def get(self, request):
        employees = Employee.objects.all()

        for employee in employees:
            one_salary = employee.salary / employee.days
            employee.salary = one_salary * (employee.days - employee.days_skipped)
            employee.salary = round(employee.salary, 2)
        return render(request, 'new_data.html', context={'employees': employees,
                                                         'is_new': True, })


class OldSalary(View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, 'new_data.html', context={'employees': employees,
                                                         'is_new': False, })


class SelectView(View):
    def get(self, request):

        return render(request, 'select.html')
