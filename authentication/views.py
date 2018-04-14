from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, LoginForm

def register_view(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            f = RegisterForm(request.POST)
            if f.is_valid():
                f.save()
                return redirect("register_success")
        else:
            return redirect("/")

    else:
        if request.user.is_authenticated:
            return redirect("/")
        else:
            f = RegisterForm()

    return render(request, 'authentication/register.html', {'form': f})


def register_sucess(request):
    return render(request, 'authentication/register_success.html')
