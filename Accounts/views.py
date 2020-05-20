from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse

def homepage(request):
    return render(request, 'Accounts/loginform.html')

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
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password']
                )
                auth.login(request, user)
                return render(request, 'Accounts/books.html')

    return render(request, 'Accounts/loginform.html')