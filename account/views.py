from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from .forms import ProfileForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return redirect('/account/profile', permanent=True)

@login_required
def profile(request):
    user = request.user
    profile_exists = Profile.objects.filter(user=user).exists()
    if profile_exists:
        profile = Profile.objects.filter(user=user).first()

    if request.method == "POST":
        if profile_exists:
            f = ProfileForm(data=request.POST, instance=profile)
        else:
            f = ProfileForm(data=request.POST)

        f.instance.user = user

        if f.is_valid():
            f.clean()
            f.save()
            messages.success(request, "Your profile has been updated")
            return redirect("/account/profile") 

    else:
        if profile_exists:
            f = ProfileForm(instance=profile)
        else:
            f = ProfileForm()

    return render(request, 'account/profile.html', {'form': f})

