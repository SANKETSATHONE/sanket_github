from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.



leave_type = (("SICK_LEAVE","sick_leave"),("EARNED_LEAVE","earned_leave"),("PRIVILAGED_LEAVE","privileged_leave"),("CASUAL_LEAVE","casual_leave"),
              ("MATERNITY_LEAVE","maternity_leave"),("PATERNITY_LEAVE","paternity_leave"),("GENERAL_ELECTION","general_election"),("MATERNITY_LEAVE","maternity_leave"))
fy_year = (("2022-2023","2022-2023"),("2021-2022","2021-2022"))

class leave_balance(models.Model):
 
    total_leave_balance = models.FloatField(validators=[MinValueValidator(0.0)])
    sick_leave_balance = models.FloatField(validators=[MinValueValidator(0.0)])
    casual_leave_balance = models.FloatField(validators=[MinValueValidator(0.0)])
    privilage_leave_balance = models.FloatField(validators=[MinValueValidator(0.0)])
    paternity_leave_balance= models.FloatField(default=1,validators=[MinValueValidator(0.0),MaxValueValidator(1.0)])
    

    def __str__(self) :
        return f"allow leave balance"

    

    
class leave(models.Model):

    leave_type = models.CharField(max_length=20, choices=leave_type)
    reason = models.TextField(verbose_name="reason of leave application",max_length=300,null=True)
    date_of_leave_applied = models.DateField(auto_now=True)
    sick_leave = models.FloatField(default=0,validators=[MinValueValidator(0.0)])
    casual_leave = models.FloatField(default=0,validators=[MinValueValidator(0.0)])
    privilage_leave = models.FloatField(default=0,validators=[MinValueValidator(0.0)])
    paternity_leave = models.FloatField(default=0,validators=[MinValueValidator(0.0),MaxValueValidator(1.0)])
    general_election = models.IntegerField(default=0,validators=[MinValueValidator(0.0),MaxValueValidator(1.0)])

    def __str__(self):
        return f"allow leave"




class holiday_leaves(models.Model):
    Financial_year= models.CharField(max_length=20, choices=fy_year)
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    
    def __str__(self) :
        return f"{self.event_name} ----> {self.event_date}"