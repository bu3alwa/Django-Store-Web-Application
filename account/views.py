from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from .forms import ProfileForm
from django.contrib import messages
from .models import Profile, Subscription
from store.models import SubscriptionModel
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

# Create your views here.

@login_required
def index(request):
    user = request.user
    sub_exists = Subscription.objects.filter(user=user).exists()

    if request.method == "POST":
        if sub_exists:
            messages.success(request, "Free Trial has expired")
            return redirect('/account')

        else:
            today = date.today()
            submodel = SubscriptionModel.objects.filter(name='Free Trial').first()
            end_date = today + timedelta(days=int(submodel.length))
            s = Subscription.objects.create(
                    user=user,
                    renew=False,
                    subscription=submodel,
                    start_date=date.today(),
                    end_date=end_date,
                    )
            s.save()

            return redirect('/account')

    else:
        if sub_exists:
            subscription = Subscription.objects.filter(user=user).order_by('-end_date').first()

            return render(request, 'account/index.html', {'user': user, 'account': subscription })

        return render(request, 'account/index.html', {'user': user })

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

@login_required
def billing(request):
    pass
