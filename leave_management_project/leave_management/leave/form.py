from leave.models import leave
from django.forms import ModelForm
from django import forms

leave_type = (("HALF_DAY", "half_day"),("FULL_DAY","full_day"))
class leave_form(ModelForm):
    
    date_of_leave_applied = forms.DateField(label="leave application date", required=True, widget =forms.DateInput(attrs={"type":"date"}))
    number_of_leaves = forms.IntegerField()
    start_Date = forms.DateField(label="from", required=True, widget =forms.DateInput(attrs={"type":"date"}))
    end_Date = forms.DateField(label="to", required=True, widget =forms.DateInput(attrs={"type":"date"}))
    type_of_leave = forms.ChoiceField(label="leave type",  choices=leave_type)
    

    class Meta:
        model = leave
        fields = "__all__"
        exclude = ["sick_leave", "casual_leave", "privilage_leave","general_election","paternity_leave"]
   
    