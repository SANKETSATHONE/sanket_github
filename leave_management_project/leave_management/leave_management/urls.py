
from django.contrib import admin
from django.urls import path
from employee.views import sign_up_user, sign_in_user, logout_user, user_leave, apply_leave, get_leave, change_password, profile_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up/',sign_up_user),
    path("sign_in/",sign_in_user),
    path("logout/",logout_user),
    path("leave/",user_leave, name="sanket"),
    path("leave_apply/", get_leave),
    path("change_pass/", change_password),
    path("profile/<str:id>", profile_page)
]

