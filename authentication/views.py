from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.

def register_view(self, request, username, password, email, firstname, lastname):
    if request.user.is_authenticated:
        u = User.objects.create_user(username, email, password)
        u.last_name = lastname
        u.first_name = firstname
        u.save()
        return redirect('/')
    else:
        return redirect('/')

def login_view(self, request, username, password):
    if not request.user.is_authenticated:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #success
            return redirect('/')
        else:
            #error
            return redirect('login')
    else:
        #render
        return render(request, 'authentication/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

