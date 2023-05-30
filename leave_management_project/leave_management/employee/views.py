from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from employee.form import OurUserForm
from django.contrib.auth import authenticate, login, logout
from employee.models import OurUser
from leave.form import leave_form
from employee.email import send_welcome_mail, send_leave_mail
from django.contrib.auth.models import User
from employee.models import OurUser
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


def sign_up_user(request):
    form = OurUserForm(request.POST)
    print("ouruser.username",request.user.username)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            print("request.POST", request.POST["username"])
            print("ouruser.username")
            send_welcome_mail(request.POST["email"],f"welcome {request.user.first_name} to agile connects")
            return render(request,"home.html")
         
        return HttpResponse("not valid")
    return render(request, 'signup.html',{"form":form})



def sign_in_user(request):
    form = AuthenticationForm(data=request.POST)
    if request.method == "POST":
        form.is_valid()
        user = OurUser.objects.get(username=request.POST["username"])
        if user:
            result =authenticate(username=request.POST["username"],
                                 password=request.POST["password"])

            if result:
                login(request,result)
                # response = redirect("/profile")
                # return response
                # redirect("/profile/<str:pk>", pk=user)
                # print("user.username",OurUser.emp_id)
                # for i in OurUser.objects.filter(username=request.POST["username"]):
                #     id=i.emp_id
                #     print("id------->", id)
                # print("ouruser.first ----->", OurUser.first_name)
                # return redirect(reverse("profile",kwargs={'str':id}))
                return HttpResponseRedirect("/profile/<str:id>".format(id=id))
                
            else:
                return HttpResponse("username or password incorrect")
        else:
            return HttpResponse("error")
    return render(request,"signin.html",{"form":form})



@login_required()
def logout_user(request):
    logout(request)
    form = AuthenticationForm(data=request.POST)
    return render(request, "signin.html", {"messgae":"user logged-out","form":form})


# @login_required(login_url='/signin.html')
def user_leave(request):
    # print("reqest.user",request.user)
    # print("request.user.username",request.user)
    data_leave = OurUser.objects.select_related("leave").filter(username=request.user)
    
            
    return render(request, "leave.html",{"form":data_leave})


def apply_leave(request):
    user_data = OurUser.objects.filter(username = request.user)
    for i in user_data:
        print(i.Apply_Leave.leave_type)
    return render(request,"apply_leave.html")


# @login_required(login_url='/signin.html')
def get_leave(request):
   
   form = leave_form(request.POST)
   if request.method == "POST":

    if form.is_valid():
        data_leave = OurUser.objects.select_related("leave").filter(username=request.user)
        for i in data_leave:
            print(i.leave.leave_type)
            if request.POST["leave_type"]== "SICK_LEAVE":
                # print("sick_leave applied")
                # print("i.no of leaves-->",request.POST["number_of_leaves"])
                i.leave.sick_leave = request.POST["number_of_leaves"]
                # print("sick_leave---->", i.leave.sick_leave)
                # print("sick_leave_blance",i.leave_balance.sick_leave_balance )
                i.leave_balance.sick_leave_balance -= int(i.leave.sick_leave)
            if request.POST["leave_type"] == "CASUAL_LEAVE":
                print("casual-->", i.leave.casual_leave)
                i.leave.casual_leave = request.POST["number_of_leaves"]
                i.leave_balance.casual_leave_balance -= int(i.leave.casual_leave)
            if request.POST["leave_type"] == "PRIVILAGED_LEAVE":
                i.leave.privilage_leave = request.POST["number_of_leaves"]
                i.leave_balance.privilage_leave_balance -= int(i.leave.privilage_leave)
            print("sick_leave_blance",i.leave_balance.sick_leave_balance )
            i.leave_balance.total_leave_balance -= (int(i.leave.sick_leave)+int(i.leave.casual_leave)+int(i.leave.privilage_leave))
            form.save()
            send_leave_mail(i.email,f"leave applied by {request.user.username}")
           
            i.leave_balance.save()
        return render(request, "leave.html",{"form":data_leave})
   return render(request, "apply_leave.html",{"form":form})
  


@login_required(login_url='/signin.html')
def change_password(request):
    form = PasswordChangeForm(request.user, request.POST)
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user =form.save(commit=False)
            password  = request.POST.get("password")
            user.set_password(password)
            form.save()
            return render(request, "change_password.html",{"form":form})
    return render(request, "change_password.html", {"form":form})

        
    
def profile_page(request,id):
    # form = OurUser.objects.get(id=request.user.emp_id)
    form = OurUser.objects.get(id=request.user.id)
    return render(request, "profile.html",{"form":form})











    
   
