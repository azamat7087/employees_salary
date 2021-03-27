from django.urls import path, include
from .views import *

urlpatterns = [
    path("", SelectView.as_view(), name="select_view"),
    path("new_salary/", ChangeSalary.as_view(), name="change_salary"),
    path("old_salary/", OldSalary.as_view(), name="old_salary"),
]
