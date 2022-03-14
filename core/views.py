from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

def register(request):
    
    form = RegisterForm(request.POST or None)
    
    if form.is_valid():
        data = form.clean()
        
        username = data['username']
        password = data['password']
        
        user = User(username=username)
        user.set_password(password)
        user.save()
        
        messages.info(request,"Account Created!")
        return redirect('login')
    
    return render(request,'auth/register.html',{'form':form})


def Login(request):
    form = LoginForm(request.POST or None)
    
    if form.is_valid():
        data = form.action()
        print(data)
        user = authenticate(request,username=data['username'],password=data['password'])
        if user is not None:
            login(request,user)
            messages.info(request,"Welcome {}".format(request.user))
            print("loged")
            return redirect('index')
        else:
            messages.info(request,"Unable To Login! try again!")       
            print("failed") 
    return render(request,'auth/login.html',{'form':form})

def Logout(request):
    logout(request)
    
    return redirect('index')

def index(request):
    
    return render(request,'core/index.html',context={})