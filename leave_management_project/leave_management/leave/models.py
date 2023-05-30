from django.db import models

# Create your models here.



leave_type = (("SICK_LEAVE","sick_leave"),("EARNED_LEAVE","earned_leave"),("PRIVILAGED_LEAVE","privileged_leave"),("CASUAL_LEAVE","casual_leave"),
              ("MATERNITY_LEAVE","maternity_leave"),("PATERNITY_LEAVE","paternity_leave"))
fy_year = (("2022-2023","2022-2023"),("2021-2022","2021-2022"))

class leave_balance(models.Model):
 
    total_leave_balance = models.IntegerField()
    sick_leave_balance = models.IntegerField()
    casual_leave_balance = models.IntegerField()
    privilage_leave_balance = models.IntegerField()

    def __str__(self) :
        return f"{self.sick_leave_balance} {self.casual_leave_balance} {self.privilage_leave_balance}"

    

    
class leave(models.Model):

    leave_type = models.CharField(max_length=20, choices=leave_type)
    reason = models.TextField(verbose_name="reason of leave application",max_length=300,null=True)
    date_of_leave_applied = models.DateField(auto_now=True)
    sick_leave = models.IntegerField(default=0)
    casual_leave = models.IntegerField(default=0)
    privilage_leave = models.IntegerField(default=0)

    
   
    


class holiday_leaves(models.Model):
    Financial_year= models.CharField(max_length=20, choices=fy_year)
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    