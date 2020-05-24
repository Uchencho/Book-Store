from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect

def homepage(request):
    return render(request, 'Accounts/loginform.html')

def home(request):
    return render(request, 'Accounts/books.html')

def signup(request):
    """
    The signup function
    """
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            username = request.POST['username']
            qs = User.objects.filter(username__iexact=username)
            if qs.exists():
                return render(request, 'Accounts/loginform.html', {'error':'Username already exists'})
            else:
                input_username = request.POST['username'].lower().strip()
                User.objects.create_user(
                    input_username,
                    password=request.POST['password']
                )
                return render(request, 'Accounts/loginform.html', {'error':'Please login'})
        else:
            return render(request, 'Accounts/loginform.html', {'error':'Password must match'})

    return render(request, 'Accounts/loginform.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['susername']
        pw = request.POST['spassword']
        user = auth.authenticate(username=username, password=pw)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/home/")
        else:
            return render(request, 'Accounts/loginform.html', {'error':'Username or Password is incorrect'})
    else:
         return render(request, 'Accounts/loginform.html')
