# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.hashers import check_password

def signup(request):
    if request.method  == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            user = User.objects.get(username=request.POST['username'])
            user.profile.college = request.POST['college']
            user.profile.major = request.POST['major']
            user.profile.save()
            # user.profile.update(user=user, college=request.POST['college'], major = request.POST['major'])
            auth.login(request, user)
            return redirect('/feeds')
        
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/feeds')
        else:
            return render(request, 'accounts/login.html', {'error' : 'username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')


    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logged_out.html')

def editaccount(request):
    if request.method  == 'POST':
        passwordbefore = request.POST['passwordbefore']
        passwordafter1 = request.POST['passwordafter1']
        passwordafter2 = request.POST['passwordafter2']
        user = request.user
        if check_password(passwordbefore, user.password) and passwordafter1 == passwordafter2:
            user.set_password(passwordafter1)
            user.profile.college = request.POST['college']
            user.profile.major = request.POST['major']
            user.profile.save()
            return redirect('/feeds')
    return render(request, 'accounts/editaccount.html')
