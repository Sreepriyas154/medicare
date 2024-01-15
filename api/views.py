from django.shortcuts import render
from django.views.generic import View
from api.forms import Loginform,Registrationform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect


# Create your views here.
def sign_in(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

class Indexview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")
    
# class Loginview(View):
#     def get(self,request,*args,**kwargs):
#         form=Loginform()
#         return render(request,"login.html",{"form":form})
# class Registerview(View):
#     def get(self,request,*args,**kwargs):
#         form=Registrationform()
#         return render(request,"register.html",{"form":form})
class Loginview(View):
    def get(self,request,*args,**kwargs):
        form=Loginform()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=Loginform(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("todo-list")
            else:
                messages.error(request,"invalid deatil")
                return render(request,"login.html",{"form":form})
            
@sign_in
def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

    

class  Registerview(View):
    def get(self,request,*args,**kwargs):
        form=Registrationform()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=Registrationform(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"your redistration has been success")
            return redirect("signin")
        else:
            messages.error(request,"registration failed")
            return render(request,"register.html",{"form":form})



