from django.shortcuts import render, redirect
from . import api
from django.contrib import messages
from django.http.response import HttpResponse
from django.contrib.auth.models import auth
from .models import MyAccountManager, User

def login(request):
    if request.method == 'GET':
        return render(request, 'COVIDtracker/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("/login")


def register(request):
    if request.method == 'GET':
        return render(request, 'COVIDtracker/register.html')
    elif request.method == 'POST':
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        confirm = request.POST.get('conpass')

        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(password=password, email=email, username=username)
                return redirect('/login')
        else:
            messages.info(request, 'Passwords Do Not Match')
            return redirect('/register')

def home(request):
    if request.method == 'GET':
        return render(request, 'COVIDtracker/home.html')
    elif request.method == 'POST':
        x = request.POST.get('user_input')
        try:
            info = x.split("-")
            return render(request, 'COVIDtracker/output.html', {'parameters': api.finder(info[1], info[0])})

        except:
            return render(request, 'COVIDtracker/output.html', {'parameters': {'ErrorCode' : 2}})

def profile(request):
    if str(request.user) != 'AnonymousUser':
        return render(request, 'COVIDtracker/profile.html', {'user': request.user})

    else:
        return render(request, 'COVIDtracker/profile.html', {'user': 'User Not Authenticated'})


def logout(request):
    auth.logout(request)
    return redirect ("/")