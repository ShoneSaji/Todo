from django.shortcuts import render,redirect
from django.views.generic import View
from work_app.forms import Register,Login,TaskForm
from work_app.models import User,Taskmodel
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator


# Create your views here.

 
def signin_required(fn):
    def wrapper(request,**kwargs):

        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,**kwargs)
    return wrapper


def mylogin(fn):
    def wrapper(request,**kwargs):

        id=kwargs.get("pk")
        obj=Taskmodel.objects.get(id=id)
        if obj.user!=request.user:
            return redirect("login")
        else:
            return fn(request,**kwargs)
    return wrapper



class Registration(View):
    def get(self,request,**kwargs):

        form=Register()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,**kwargs):
        form=Register(request.POST)
        if form.is_valid():
            # form.save()
            # form=Register()
            # return render(request,"index.html",{"form":form})    
            User.objects.create_user(**form.cleaned_data)
            form=Register()
            # return render(request,"register.html",{"form":form})
            return redirect("login")



class Update_user(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        data=User.objects.get(id=id)
        form=Register(instance=data)
        return render(request,"register.html",{"form":form})


    def post(self,request,**kwargs):
        id=kwargs.get("pk")
        data=User.objects.get(id=id)
        form=Register(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect("login")



class Logging(View):
    def get(self,request,**kwargs):
        form=Login()
        return render(request,"login.html",{"form":form})        


    def post(self,request,**kwargs):
        form=Login(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

            u_name=form.cleaned_data.get("username")

            pwd=form.cleaned_data.get("password")

            user_obj=authenticate(username=u_name,password=pwd)

            if user_obj:

                print("Valid Credentials")
                login(request,user_obj)
                return redirect("add")
            else:
                print("incorrect credentials")
                return render(request,"login.html")
            
            

@method_decorator(signin_required,name='dispatch')
class Add_Task(View):

    def get(self,request):
        form=TaskForm()
        data=Taskmodel.objects.filter(user=request.user).order_by('completed') 
        # order_by('completed')==>used to pop up the uncompleted to first and completed to down ,here completed is a field. 
        return render(request,"add.html",{"form":form,"data":data})
    
    def post(self,request):
        form=TaskForm(request.POST)

        if form.is_valid():
            form.instance.user=request.user
            # request.user=get the authencated user(login)
            messages.success(request,"Task added successfully")
            form.save()
            form=TaskForm()
        data=Taskmodel.objects.filter(user=request.user).order_by('completed') #==> read  method
        return render(request,"add.html",{"form":form,"data":data})
        
@method_decorator(signin_required,name='dispatch')
@method_decorator(mylogin,name='dispatch')
class Delete_Task(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        Taskmodel.objects.get(id=id).delete()
        return redirect("add")
    

class Task_Edit(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")  
        obj=Taskmodel.objects.get(id=id)
        
        if obj.completed == False:
            # completed is a field in model
            obj.completed = True
            print(obj.completed)
            obj.save()
        return redirect("add")    


class Signout(View):
    def get(self,request):
        logout(request)
        return redirect('login')    


class User_Delete(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        User.objects.get(id=id).delete()
        return redirect("home")       
    