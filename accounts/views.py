from django.shortcuts import render
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import Account




# Create your views here.

def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are logged in')
            request.session['email']=email
            request.session['name']=user.name
            # store user details in session
            request.session['district']=user.district
            return redirect('home')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        name=request.POST['name']
        mun_name=request.POST['mun_name']
        username=request.POST['username']
        state=request.POST['state']
        district=request.POST['district']
        role=request.POST['role']
        phone_number=request.POST['tel']
        print(email,password,name,username,state,district,role,phone_number)
        if Account.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('register')
        elif Account.objects.filter(username=username).exists():
            messages.error(request, 'username already exists')
            return redirect('register')
        else:
            user=Account.objects.create_user(email=email, password=password, name=name, username=username, state=state, district=district, role=role, phone_number=phone_number, mun_name=mun_name)
            user.save()
            messages.success(request, 'you are registered')
            return redirect('login')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')