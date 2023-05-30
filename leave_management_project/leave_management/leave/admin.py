from django.contrib import admin
from leave.models import leave_balance, leave, holiday_leaves
# Register your models here.
admin.site.register(leave_balance)
admin.site.register(leave)
admin.site.register(holiday_leaves)