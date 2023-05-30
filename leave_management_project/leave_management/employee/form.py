from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from employee.models import Employee
from employee.models import OurUser
from django import forms

class OurUserForm(UserCreationForm):
    class Meta:
        model=OurUser
        fields = ["emp_image","emp_id","username","first_name","last_name","email","password1","department", "role","gender","department",
                  "designation","role","marital_status","fy_year","leave_balance","leave","reporting_manager_name"]
