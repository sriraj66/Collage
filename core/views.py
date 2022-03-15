import uuid
from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from .models import Students
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .helper import *

def register(request):
    
    form = RegisterForm(request.POST or None)
    
    if form.is_valid():
        data = form.clean()
        
        username = data['username']
        password = data['password']
        
        user = User(username=username)
        user.set_password(password)
        user.save()
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

def Password_Link(request):
    
    if request.method == 'POST':
        m = request.POST.get('mail');
        uid = str(uuid.uuid4())
        
        profile = Students.objects.filter(mail=m)
        profile.update(token=uid)
        print(profile[0])
        url = request.build_absolute_uri('passwordReset/{}'.format(profile[0].token))
        print(url)
        msg = "Kindly Click The link And reset Your Password click {}".format(url)
        mail(m,"Your Reset Email For Collage",str(msg))
        # return redirect('reset_pass',uid)
        
        
    return redirect('login')

def Password_reset(request,token):
    std = Students.objects.filter(token=token)
    if len(std)!=0:
        if request.method == 'POST':
            p1 = request.POST.get('p1')
            p2 = request.POST.get('p2')
            print(std)
            user = User.objects.get(username=std[0].user.username)
            std.update(token=str(uuid.uuid4()))
            if p1==p2:
                user.set_password(p1.upper())
                user.save()
                messages.success(request,"password reseted")
                return redirect('login')
            else:
                messages.error(request,"Password Not Maching")
    else:
        messages.error(request,"URL Expired")
        return redirect('login')
    return render(request,'auth/passwordreset.html',{'token':token})

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
        data = Students.objects.filter(user=request.user)
        if len(data)>0:
            return render(request,'core/index.html',{'data':data[0]})

    return render(request,'core/index.html')
