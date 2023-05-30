from django.db import models
from django.contrib.auth.models import User
from leave.models import leave_balance, leave, holiday_leaves

# Create your models here.


department = (("DEVELOPMENT","development"), ("BACK_OFFICE", "back_office"),("DISPTCH","dispatch"),("FIELD_ENGINEERS","field_engineers"),("ACCOUNTS","accounts"))
role_choice = (("MASTER","master"),("MANAGER","MANAGER"),("TEAM_MEMBER","team_member"), ("FIELD_WORKER","field_worker"))
marital_status = (("MARRIED","married"),("UNMARRIED","unmarried"))
gender_choice = (("MALE","male"), ("FEMALE","female"))
fy_year = (("2022-2023","2022-2023"),("2021-2022","2021-2022"))

class OurUser(User):
    class Meta:
        db_table = "Our_user"
    
    emp_image = models.ImageField(upload_to='upload/', null=True, blank=True)
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=gender_choice)
    department = models.CharField(max_length=20,choices=department,default="add department")
    designation = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=role_choice, null=True)
    marital_status = models.CharField(max_length=50, choices=marital_status)
    fy_year = models.CharField(max_length=20, choices=fy_year)
    leave_balance = models.ForeignKey(leave_balance, on_delete=models.CASCADE,null=True,blank=True)
    leave = models.ForeignKey(leave, on_delete=models.CASCADE, null=True, blank=True)
    holiday_leaves = models.ForeignKey(holiday_leaves, on_delete=models.CASCADE,null=True)
    reporting_manager_name = models.CharField(max_length=25)

    
    def __str__(self) :
        return f"{self.first_name}"



 