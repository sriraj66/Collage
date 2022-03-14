import profile
from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from .models import Students
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
        u = authenticate(request,username=username,password=password)
        if u is not None:
            login(request,u)
        
        messages.info(request,"Account Created!")
        return redirect('profile')
    
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

def Profile(request):

    if request.method == 'POST':
        user = request.user
        
        regno = request.POST.get('regno')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        mail = request.POST.get('mail')
        date = request.POST.get('date')
        profile = Students.objects.filter(user=user)
        profile.update(reg_num=regno,name=name,phone=phone,dob=date,mail=mail)
        messages.success(request,"Profile Updated")
        return redirect('index')
    return render(request,'auth/profile.html',{})

def index(request):
    if request.user.is_authenticated:
        data = Students.objects.filter(user=request.user)[0]
        print(data)
        return render(request,'core/index.html',{'data':data})

    return render(request,'core/index.html')
